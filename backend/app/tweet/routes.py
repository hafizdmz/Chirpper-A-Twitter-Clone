from flask import request, jsonify, make_response, send_file, send_from_directory
from app.extensions import db

from app.tweet import tweetBp
from app.models.tweet import Tweets
from app.models.user import Users

from flask_jwt_extended import jwt_required, get_jwt_identity

from datetime import timedelta

from werkzeug.utils import secure_filename
import os

from minio import Minio

client = Minio(
    "play.min.io",
    access_key="Q3AM3UQ867SPQQA43P2F",
    secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
)

UPLOAD_FILE_LOCATION = './static/uploaded/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
BUCKET_NAME = 'dmzimage'

def allowed_file(filename):
    """
    Cek apakah format file yang diupload benar
    """
    filename = filename.lower()
    extension = filename.split(".")[-1]

    return extension in ALLOWED_EXTENSIONS

@tweetBp.route("", methods=['GET'], strict_slashes = False)
@jwt_required(locations=["headers"],optional=True)
def get_tweet():
    limit = request.args.get('limit', 20)
    if type(limit) is not int:
        return jsonify({'message': 'invalid parameter'}), 400
    
    user_id = get_jwt_identity()

    if not user_id:
        user_id = "None"
    else:
        user_id = user_id

    # get tweets by id
    tweets = db.session.execute(
        db.select(Tweets).limit(limit)
    ).scalars()

    results = []
    for tweet in tweets:
        results.append(tweet.serialize())

    response = make_response(jsonify(
        user_id = user_id,
        data=results
    ), 200)
    # response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@tweetBp.route("", methods=['POST'], strict_slashes = False)
@jwt_required(locations=["headers"])
def post_tweet():

    # Check bucket name.
    found = client.bucket_exists(BUCKET_NAME)
    if not found:
        client.make_bucket(BUCKET_NAME)
    else:
        print(f"Bucket '{BUCKET_NAME}' already exists")

    # cek apakah terdapat file didalam post
    if 'file' in request.files:

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No File Selected'}), 422

        if file and allowed_file(file.filename):
            content = request.form.get("content")
            user_id = get_jwt_identity()
            image_size = os.fstat(file.fileno()).st_size
            # created_at = datetime.now()
            image_name = secure_filename(file.filename)
            client.put_object(BUCKET_NAME, 
                              image_name, 
                              file, 
                              image_size)
            image_path = client.presigned_get_object(BUCKET_NAME,
                                                     image_name,
                                                     expires=timedelta(days=7))
            new_content = Tweets(content=content,
                                 user_id=user_id,
                                 image_name=image_name,
                                 image_path=image_path)

            db.session.add(new_content)
            db.session.commit()
            response = make_response(
                jsonify(data=new_content.serialize()), 200)

            return response

    data = request.get_json()
    content = data.get('content', None)

    if not content:
        return jsonify({'error': 'Invalid data'}), 422
    
    user_id = get_jwt_identity()

    tweet = Tweets(
        user_id = user_id,
        content=content
    )
    db.session.add(tweet)
    db.session.commit()

    # make response
    response = make_response(jsonify(data=tweet.serialize()), 200)
    # konfigurasi CORS dari respponse
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers['Content_Type'] = 'application/json'
    return response

def serve_image(filename):
    """
    Serve uploaded image
    """

    img_directory = './static/uploaded'
    image_path = os.path.join(img_directory, filename)
    return image_path

@tweetBp.route("/image/<string:name>", strict_slashes=False)
@jwt_required(locations=["headers"], optional=True)
def get_image(name):
    image_name = name
    img = serve_image(image_name)
    return send_file(img)


@tweetBp.route("/download/<string:name>", strict_slashes=False)
@jwt_required(locations=["headers"], optional=True)
def download_image(name):
    return send_from_directory(UPLOAD_FILE_LOCATION, name)
