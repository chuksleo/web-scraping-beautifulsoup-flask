from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Department, Role, Crawl


class DepartmentForm(FlaskForm):
	"""
	Form for admin to add or delete a department
	"""
	name = StringField('Name', validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])
	submit = SubmitField('Submit')

class RoleForm(FlaskForm):
	"""
	Form for admin to add or edit role
	"""
	name = StringField('Name', validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])
	submit = SubmitField('Submit')

class UserAssignForm(FlaskForm):
	"""
	Form for admin to assign role for employees
	"""
	department = QuerySelectField(query_factory=lambda: Department.query.all(), get_label="name")
	role = QuerySelectField(query_factory=lambda: Role.query.all(), get_label="name")
	submit = SubmitField('Submit')




class CrawlForm(FlaskForm):
	"""
	Form for setting crwal url and crawl	"""
	
	content = StringField('Content', validators=[DataRequired()])
	site = SelectField(u'Crawl Site', choices=[('jiji', 'Jiji'),('car45','Car45')])
	submit = SubmitField('Submit')