from flask import request, jsonify, make_response
from app.extensions import db

from app.tweet import tweetBp
from app.models.tweet import Tweets
from app.models.user import Users

from flask_jwt_extended import jwt_required, get_jwt_identity

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
