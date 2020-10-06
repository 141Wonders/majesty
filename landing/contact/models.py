import datetime
from landing import db

class EmailSignup(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(60))
	last_name = db.Column(db.String(60))
	email = db.Column(db.String(60), unique=True, nullable=False)
	phone_number = db.Column(db.Integer())
	timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)

	def save(self, commit=True):
		# create and update database entries
		if commit:
			instance = self
			if not instance.id:
				db.session.add(instance)
			try:
				db.session.commit()
			except Exception as e:
				print("Exception occured\n", e, '\n')
				db.session.rollback()
				return False
			return True
		return False

	def delete(self, commit=True):
		# delete database entries
		if self.id:
			db.session.delete(self)
			try:
				db.session.commit()
			except Exception as e:
				print("Exception occured\n", e, '\n')
				db.session.rollback()
				return False
			return True
		return False
