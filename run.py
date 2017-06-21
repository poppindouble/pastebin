from app import app
from flask import make_response, jsonify, request
from pymongo import MongoClient
import datetime
from hashlib import md5

client = MongoClient()
db = client["test_paste"]

@app.route("/")
def hello():
	return "Welcome to pastebin!"

@app.route("/api/v1/paste", methods=['POST'])
def create_paste():
	ip_address = request.remote_addr
	time_stamp = datetime.datetime.now().strftime("%B %d, %Y")
	hashUrl = md5(ip_address + time_stamp).digest().encode('base64')[:7]

	return jsonify({
		"url": hashUrl
		})

	# result = db.datasets.insert_one({
	# 	"content": "1",
	# 	"testing": "my 3 insert"
	# 	})
	# print(result.inserted_id)
	# return "response from create"

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
	app.run(debug=app.debug)