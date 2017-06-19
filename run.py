from app import app
from flask import make_response, jsonify
from pymongo import MongoClient

client = MongoClient()
db = client["test_paste"]

@app.route("/")
def hello():
	return "Hello World!!!"

@app.route("/create")
def create():
	result = db.datasets.insert_one({
		"content": "1",
		"testing": "my 3 insert"
		})
	print(result.inserted_id)
	return "response from create"

@app.route("/all")
def get_all():
	cursor = db.datasets.find()
	for document in cursor:
		print(document)
	return "all"

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
	app.run(debug=app.debug)