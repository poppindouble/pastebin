from app import app, db
from flask import make_response, jsonify, request
from pymongo import MongoClient
import datetime
from hashlib import md5
from app.models import Paste
from bson.objectid import ObjectId

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
	result = mongodb["pastes"].insert_one({
		"content": text_content
		})
	if result.acknowledged:
		try:
			paste = Paste(hashUrl, 60, time_stamp, str(result.inserted_id))
			db.session.add(paste)
			db.session.commit()
		except:
			result = mongodb["pastes"].delete_one({'_id': ObjectId(result.inserted_id)})
			return make_response(jsonify({'error': 'Can not insert'}), 404)

		return jsonify({
			"url": hashUrl
			})
	else:
		return make_response(jsonify({'error': 'Can not insert'}), 404)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
	app.run(debug=app.debug)