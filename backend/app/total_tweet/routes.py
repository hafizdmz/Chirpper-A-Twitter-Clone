from app.total_tweet import totalTweetBp
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify, make_response

from app.extensions import db

from app.models.countTweet import CountTweet

@totalTweetBp.route("", methods=['GET'], strict_slashes = False)
@jwt_required(locations=["headers"],optional=True)
def get_total_tweet():
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
        db.select(CountTweet).limit(limit)
    ).scalars()

    results = []
    for tweet in tweets:
        results.append(tweet.serialize())

    response = make_response(jsonify(
        user_id = user_id,
        data=results
    ), 200)
    return response