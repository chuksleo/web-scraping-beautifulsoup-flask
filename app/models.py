from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


class User(UserMixin, db.Model):
	"""
	Create an Employee Table
	"""

	__tablename__='users'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(60), index=True, unique=True)
	username = db.Column(db.String(60), index=True, unique=True)
	first_name = db.Column(db.String(60), index=True)
	last_name = db.Column(db.String(60), index=True)
	password_hash = db.Column(db.String(128))
	department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	is_admin = db.Column(db.Boolean, default=False)

	@property
	def password(self):
		"""
		Prevent password from being accessed
		"""
		raise AttributeError('pass word is not readable attribute')

	@password.setter
	def password(self, password):
		# Set Password to a hashed password
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		"""
		Check if hashed password matches actual password 
		"""
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return "<User: {}>".format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class Department(db.Model):
	"""
	Create a Department table
	"""

	__tablename__ = 'departments'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True)
	description = db.Column(db.String(200))
	users = db.relationship('User', backref='department', lazy='dynamic')

	def __repr__(self):
		return "<Department: {}>".format(self.name)


class Role(db.Model):

	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True)
	description = db.Column(db.String(200))
	users = db.relationship('User', backref='role', lazy='dynamic')

	def __repr__(self):
		return '<Role: {}>'.format(self.name)





class Crawl(db.Model):

	
	__tablename__ = 'crawls'	
	id = db.Column(db.Integer, primary_key=True, index=True)	
	content = db.Column(db.String(600))	
	price_title = db.Column(db.String(60), index=True)
	is_boost = db.Column(db.String(10))	
	product_id = db.Column(db.Integer)	
	user_id = db.Column(db.Integer)	
	region_slug = db.Column(db.String(60), index=True)	
	tops_count = db.Column(db.Integer)	
	as_top = db.Column(db.String(10))	
	user_phone = db.Column(db.String(60), index=True)	
	region_name = db.Column(db.String(100), index=True)
	price = db.Column(db.Integer)
	short_description = db.Column(db.Text)
	is_top = db.Column(db.String(10))
	date = db.Column(db.String(100), index=True)
	slug = db.Column(db.String(200))
	url = db.Column(db.String(255), index=True)
	title = db.Column(db.String(100), index=True)
	images_count = db.Column(db.Integer)
	conditions = db.Column(db.String(60), index=True)
	transmission = db.Column(db.String(60), index=True)	
	mileage = db.Column(db.String(255))
	site = db.Column(db.String(255), index=True)
	image = db.Column(db.String(100), index=True)
	image_list = db.Column(db.Text)
	year = db.Column(db.String(100), index=True)
	
	


	def __repr__(self):
		return '<Crawl: {}>'.format(self.title)
