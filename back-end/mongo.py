import datetime
from flask import Flask, request
from bson.json_util import dumps
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient()
db = client['5_love_languages']
collection = db.results


@app.route('/addResult', methods=['POST'])
def add_result():
    result = request.get_json()

    # insert result into mongo.
    post_id = collection.insert_one(result).inserted_id

    print("added {}.".format(post_id))
    return dumps({'status': 'success'})


@app.route('/readResults', methods=['GET'])
def read_results():
    results = []

    # get all results from mongo.
    for result in collection.find():
        results.append(result)
    print(results)

    return dumps({"result": results})


if __name__ == '__main__':
    app.run(debug=True)
