from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresq1://meet:123456@localhost/meet_db'
db = sqlalchemy(app)

class Pizzas(db.Model):
	__Tablename__="Pizzas"
	id = db.Column('id', db.Integer, primary_key=True)
	ordered_by = db.Column('ordered_by', db.Unicode)
	size = db.Column('size', db.Integer)

db.create_all()
