import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get the path to the data directory relative to the script's location
data_directory = os.path.join(os.path.dirname(__file__), 'data')

# Ensure the data directory exists
os.makedirs(data_directory, exist_ok=True)

# Set the SQLite database URI (consistent with the data directory path)
database_path = os.path.join(data_directory, 'cv_database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy database instance
db = SQLAlchemy(app)

# Define the CV model
class CV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    profile_summary = db.Column(db.Text)
    skills = db.Column(db.Text)
    experience = db.Column(db.Text)
    projects = db.Column(db.Text)

# Define your routes below
@app.route('/')
def index():
    cv_info = CV.query.first()  # Retrieve the first CV entry from the database
    return render_template('index.html', cv_info=cv_info)

@app.route('/cv')
def cv():
    return render_template('cv.html')

# Use app.app_context() to create tables within the Flask application context
with app.app_context():
    # Create the database tables
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
