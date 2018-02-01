from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
	return '<h1>Hello, bruh!</h1>'

@app.route('/food')

def my_favorite_food():
	return 'My favorite food from all my travel experience would be the original italian pizza I had in Sardinia'

@app.route('/user/<username>')
def show_user_name(username):
	return username

