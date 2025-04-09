from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
print(MONGO_URI)

if not MONGO_URI:
    raise ValueError("MongoDB URI is not set in the .env file!")

client = pymongo.MongoClient(MONGO_URI)
db = client.test

collection = db['flask']

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.json)
    collection.insert_one(form_data)
    return 'Data submitted successfully!'

@app.route('/view')
def view():

    data=collection.find()
    data=list(data)
    for item in data:
        print(item)
        del item['_id']
    data={
        'data':data
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000,debug=True)