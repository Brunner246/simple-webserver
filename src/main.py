from flask import Flask, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['exampleDB']
mydb = db["mydatabase"]
records = mydb["exampleCollection"]


class Cache:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def remove(self, key):
        if key in self.data:
            del self.data[key]


class MyApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.cache = Cache()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/api', methods=['POST'])
        def post_data():
            data = request.get_json()
            print(data)
            if data:
                key = "1234556"
                value = data
                records.update_one({key: {"$exists": True}}, {"$set": {key: value}}, upsert=True)
                self.cache.add(key, value)
            return jsonify({"received": data}), 200

        @self.app.route('/api', methods=['GET'])
        def get_data():
            data = list(records.find({}, {'_id': False}))
            return jsonify(data)

        @self.app.route('/', methods=['GET'])
        def index():
            with open('index.html') as f:
                return f.read()

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    my_app = MyApp()
    my_app.run()
