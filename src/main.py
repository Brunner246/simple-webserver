from flask import Flask, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['exampleDB']

app = Flask(__name__)

my_data = "Hello, World!"

mydb = db["mydatabase"]
records = mydb["exampleCollection"]


@app.route('/api', methods=['GET'])
def get_data():
    data = list(records.find({}, {'_id': False}))
    return jsonify(data)


@app.route('/api', methods=['POST'])
def post_data():
    data = request.get_json()
    print(data)
    if data:
        key = "1234556"
        value = data
        records.update_one({key: {"$exists": True}}, {"$set": {key: value}}, upsert=True)
    return jsonify({"received": data}), 200


@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>My Page</title>
            <style>
                body {
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                h1 {
                    color: #333;
                }
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)
