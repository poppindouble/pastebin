from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client["test_paste"]

@app.route("/")
def hello():
	return "Hello World!"

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
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)