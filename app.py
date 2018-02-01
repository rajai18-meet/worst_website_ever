from flask import Flask, render_template, request

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku

app = Flask(__name__)

#from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'

heroku = Heroku(app)
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(80), unique=True, nullable=False)
   
	def __init__(self, username, password):
		self.username=username
		self.password=password

db.create_all()

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/worldmap')
def worldmap():
	return render_template('worldmap.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/best_deals')
def best_deals():
	return render_template('best_deals.html')


@app.route('/login', methods=['POST'])
def login():
	print ('hi')
	username = request.form['username']
#	user = user.query.
	password = request.form['password']
	return render_template('home.html', username=username)

@app.route('/signup', methods=['POST',"GET"])
def signup():
	if request.method == "GET":
		return render_template('signup.html')
	elif request.method == "POST":
		user= User(username= request.form['name'], password= request.form['password'])
		db.session.add(user)
		username=user.username
		return render_template('home.html', username=username)




if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
   app.run(debug = True)


# DATABASE START

