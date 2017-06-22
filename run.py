from app import app, db
from flask import make_response, jsonify, request
from pymongo import MongoClient
import datetime
from hashlib import md5
from app.models import Paste

client = MongoClient('localhost', 27017)
mongodb = client["pastebin"]

@app.route("/")
def hello():
	return "Welcome to pastebin!"

@app.route("/api/v1/paste", methods=['POST'])
def create_paste():
	ip_address = request.remote_addr
	time_stamp = datetime.datetime.now().strftime("%B %d, %Y")
	hashUrl = md5(ip_address + time_stamp).digest().encode('base64')[:7]
	text_content = request.form['content']
	# store to mongodb to get result.inseredid
	result = mongodb["pastes"].insert_one({
		"content": text_content
		})
	print(result.inserted_id)
	try:
		paste = Paste(hashUrl, 60, time_stamp, str(result.inserted_id))
		db.session.add(paste)
		db.session.commit()
	except:
		return make_response(jsonify({'error': 'Can not insert'}), 404)

	return jsonify({
		"url": hashUrl
		})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
	app.run(debug=app.debug)