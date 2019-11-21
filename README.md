# Simple CRUD app using Flask With Sample BeautifulSoup Integration

A simple CRUD (Create, Read, Update, Delete) user management web app using Flask + MySQL. This is not my original work. I follow a tutorial [here](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)



For the BeautifulSoup Implemetation
====================================

If you are new to webscraping and you have decided to try our BeautifulSoup then you can use this as a starting point to understand how you can play arround with BeautifulSoup after getting content from a page. For this project am scraping data from https://jiji.ng/cars and https://buy.cars45.com/cars



Running project
=====================
Create database base in Mysql with name "crud"

change Mysql connection settings in instance/config.py to your preferred settings

pip -install -r requirments.txt

Export the flowing enviroment variable :
export FLASK_CONFIG=development
export FLASK_APP=run.py


-Run Migrations
	flask db stamp head
  flask db migrate
  flask db upgrade

then run: python run.py

- Register a user
- then run the following query on your db console : "update users set is_admin=1 where id=1;
	this will give you access to the admin menus(just wanted to be quick on that)

Cheers!
