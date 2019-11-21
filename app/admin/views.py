from flask import abort, flash, redirect, url_for, render_template

from flask_login import current_user, login_required

from . import admin
from forms import DepartmentForm, RoleForm, UserAssignForm, CrawlForm
from .. import db
from ..models import Department, Role, User, Crawl
import requests
from bs4 import BeautifulSoup
import json, re


def check_admin():
	"""
	Prevent a non admin access
	"""
	if not current_user.is_admin:
		abort(403)

# Department views

@admin.route('/deparments', methods=['GET', 'POST'])
@login_required
def list_departments():
	"""
	List all departments
	"""
	check_admin()
	departments = Department.query.all()
	print departments
	return render_template('admin/departments/departments.html',
							departments=departments, title = 'Departments')


@admin.route('/deparments/add', methods=['GET', 'POST'])
@login_required
def add_department():
	"""
	add deparment to the database
	"""
	check_admin()
	add_department = True
	form = DepartmentForm()
	if form.validate_on_submit():
		department = Department(name=form.name.data, description=form.description.data)
		try:
			#add department to the database
			db.session.add(department)
			db.session.commit()
			flash('You have successfully created a deparment')
		except:
			#in case department name already exists
			flash('Error : Department name already exists')
		#redirect to departments page
		return redirect(url_for('admin.list_departments'))

	# load the department template
	return render_template('admin/departments/department.html', action ="Add", add_department=add_department, form=form, title="Add Department")

@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
	"""
	Edit a department
	"""
	check_admin()

	add_department = False
	department = Department.query.get_or_404(id)
	form = DepartmentForm(obj=department)
	if form.validate_on_submit():
		department.name = form.name.data
		department.description = form.description.data
		db.session.commit()
		flash('You have successfully edited the department')

		# return to the departments page
		return redirect(url_for('admin.list_departments'))

	form.description.data = department.description
	form.name.data = department.name
	return render_template('admin/departments/department.html', action="Edit", add_department=add_department, form=form, department=department, title="Edit Department")

@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
	"""
	Delete a department from the database
	"""
	check_admin()

	department = Department.query.get_or_404(id)
	db.session.delete(department)
	db.session.commit()
	flash('You have successfully deleted the department.')

	# redirect to the departments page
	return redirect(url_for('admin.list_departments'))

	return render_template(title="Delete Department")


@admin.route('/roles')
@login_required
def list_roles():
	check_admin()
	"""
	List all roles
	"""
	roles = Role.query.all()
	return render_template('admin/roles/roles.html', roles=roles, title='Roles')

@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
	"""
	Add a role to the database
	"""
	check_admin()
	add_role = True

	form = RoleForm()
	if form.validate_on_submit():
		role = Role(name=form.name.data, description=form.description.data)
		try:
			# add role to the database
			db.session.add(role)
			db.session.commit()
			flash('You have succesfully added one role.')
		except:
			# in case role name already exists
			flash('Error: Role already exists')

		#redirect to the list roles page
		return redirect(url_for('admin.list_roles'))

	# load the role template
	return render_template('admin/roles/role.html', add_role=add_role, form=form, title='Add role')

@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
	"""
	Edit a role
	"""
	check_admin()

	add_role = False

	role = Role.query.get_or_404(id)
	form = RoleForm(obj=role)
	if form.validate_on_submit():
		role.name = form.name.data
		role.description = form.description.data
		db.session.add(role)
		db.session.commit()
		flash('You have successfully edited the role.')

		# redirect to the roles page
		return redirect(url_for('admin.list_roles'))

	form.description.data = role.description
	form.name.data = role.name
	return render_template('admin/roles/role.html', add_role=add_role,
						   form=form, title="Edit Role")

@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
	"""
	Delete a role from the database
	"""
	check_admin()

	role = Role.query.get_or_404(id)
	db.session.delete(role)
	db.session.commit()
	flash('You have successfully deleted the role.')

	# redirect to the roles page
	return redirect(url_for('admin.list_roles'))

	return render_template(title="Delete Role")

@admin.route('/users')
@login_required
def list_users():
	"""
	List all users
	"""
	check_admin()
	users = User.query.all()
	return render_template('admin/users/users.html', users=users, title='users')

@admin.route('/users/assign/<int:id>', methods=['GET','POST'])
@login_required
def assign_user(id):
	"""
	Assign user to department
	"""
	check_admin()
	user = user.query.get_or_404(id)
	print "this is:"
	print(user)

	form = userAssignForm(obj=user)
	if form.validate_on_submit():
		user.department = form.department.data
		user.role = form.role.data
		db.session.add(user)
		db.session.commit()
		flash('You have successfully assigned a department and role.')

		# redirect to the roles page
		return redirect(url_for('admin.list_users'))

	return render_template('admin/users/user.html', user=user, form=form, title='Assign user')


@admin.route('/crawl', methods=['GET', 'POST'])
@login_required
def crawl_page():
	check_admin()


	form = CrawlForm()
	if form.validate_on_submit():
		crawl = Crawl(content=form.content.data)
		site = Crawl(content=form.site.data)
		if site.content == "jiji":
			print "RUNINI JIJI"
			Crawl_Jiji(crawl, site)
		else:
			print "RUNINI CAR45"
			Crawl_CarFF(crawl, site)


	return render_template('admin/crawl/crawl.html', form=form, title='Crawl Sites')



def Crawl_CarFF(crawl, site):
	cdata = requests.get(crawl.content)
	soup = BeautifulSoup(cdata.text, 'html.parser')
	data = []


	for div in soup.find_all('div', {'class': 'product_box'}):
		f = []
		title = [h4.text for h4 in div.find_all('h4')]
		condition = [p.text for p in div.find_all('p', {'class': 'car-origion'})]
		priceval = [h5 for h5 in div.find_all('h5')[0]]
		details = [span.text for span in div.find_all('span', {'class': 'intersemibold'})]
		sellval = [p.text for p in div.find_all('p', {'class': 'text-muted'})]
		seller = ' '.join(sellval[0].split())
		lenval = len(details)
		year = ''
		mileage = ''
		product_id = ''
		if lenval == 3 :
			mileage = details[0]
			year = details[1]
			product_id = details[2]
		else:
			if details[0].find('km') == -1:
				mileage = 'None'
				year = details[0]
			else:
				mileage = details[0]
				year = 'None'

			product_id = details[1]



		price = ' '.join(priceval[0].split())
		seller = ' '.join(seller.split())
		content = "This car is a very sound neat car with all features crwlwed from jiji online market place"
		price_title = str(price[1:])
		isboost = "none"
		productid = product_id.split('-')[1]
		userid = 0
		region_slug = seller
		tops_count = 0
		as_top = ""
		user_phone = "None"
		region_name = seller
		price = 0
		short_description = ""
		is_top = ""
		date = ""
		slug = ""
		url = ""
		title = title
		images_count = 0
		conditions = condition
		transmission = ""
		mileage = str(mileage)
		site = str(site)
		image = ""
		image_list = ""
		car = Crawl(content=content, price_title=price_title, is_boost=isboost, product_id=productid, user_id=userid, region_slug=region_slug, tops_count=tops_count, as_top=as_top, user_phone=user_phone, region_name=region_name, price=price, short_description=short_description, is_top=is_top, date=date, slug=slug, url=url, title=title, images_count=images_count, conditions=conditions, transmission=transmission, mileage=mileage, site=site, image=image, image_list=image_list)
		db.session.add(car)
		db.session.commit()
		flash('You have succesfully added one car.')


def Crawl_Jiji(crawl, site):
	cdata = requests.get(crawl.content)
	soup = BeautifulSoup(cdata.text, 'html.parser')
	newDictionary=json.loads(str(soup))
	ads = newDictionary['adverts_list']
	adverts = ads['adverts']




	try:



		for advert in adverts:

			content = "This car is a very sound neat car with all features crwlwed from jiji online market place"
			price_title = re.sub(r'\W+', ' ', advert['price_title'])
			isboost = advert['is_boost']
			productid = advert['id']
			userid = advert['user_id']
			region_slug = advert['region_slug']
			tops_count = advert['tops_count']
			as_top = advert['as_top']
			user_phone = advert['user_phone']
			region_name = advert['region_name']
			price = advert['price']
			short_description = str(advert['short_description'])
			is_top = advert['is_top']
			date = advert['date']
			slug = advert['slug']
			url = advert['url']
			title = advert['title']
			images_count = advert['images_count']
			conditions = advert['attributes'][0][1]
			transmission = advert['attributes'][1][1]
			mileage = advert['attributes'][2][1]
			site = site
			image = advert['image']
			image_list = str(advert['image_list'])
			car = Crawl(content=content, price_title=price_title, is_boost=isboost, product_id=productid, user_id=userid, region_slug=region_slug, tops_count=tops_count, as_top=as_top, user_phone=user_phone, region_name=region_name, price=price, short_description=short_description, is_top=is_top, date=date, slug=slug, url=url, title=title, images_count=images_count, conditions=conditions, transmission=transmission, mileage=mileage, site=site, image=image, image_list=image_list)
			db.session.add(car)
			db.session.commit()
			flash('You have succesfully added one car.')



	except:
			# in case car name already exists
			flash('Error: Car already exists')
