from app import db

class Paste(db.Model):
	shortlink = db.Column(db.String(7), primary_key=True, nullable=False)
	expiration_length_in_minutes = db.Column(db.Integer, nullable=False)
	created_at = db.Column(db.DateTime, nullable=False)
	paste_path = db.Column(db.String(255), nullable=False)

	def __init__(self, shortlink, expiration_length_in_minutes, created_at, paste_path):
		self.shortlink = shortlink
		self.expiration_length_in_minutes = expiration_length_in_minutes
		self.created_at = created_at
		self.paste_path = paste_path

	def __repr__(self):
		return '<Paste %r>' % (self.shortlink)