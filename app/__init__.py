from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'  # Adjust this to your DB
db = SQLAlchemy(app)

# Import routes after initializing app and db
from app import routes

