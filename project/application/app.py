import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from script import fetch_cv_data  # Import the fetch_cv_data function

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

class CV(db.Model):
    __tablename__ = 'cv_data'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    location = db.Column(db.String(100))
    education = db.Column(db.Text)
    skills = db.Column(db.Text)
    experience = db.Column(db.Text)
    projects = db.Column(db.Text)
    github = db.Column(db.String(100))

if not os.path.isfile(database_path):
    with app.app_context():
        db.create_all()

# Define your routes below
@app.route('/')
def index():
    try:
        cv_data = fetch_cv_data(database_path)  # Use fetch_cv_data function
        if cv_data:
            return render_template('index.html', cv_info=cv_data)
        else:
            return render_template('index.html', name="Default Name", cv_info=None)
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Modify the cv route in your Flask app (app.py)
@app.route('/cv')
def cv():
    try:
        # Fetch data from the database
        cv_data = fetch_cv_data(database_path)

        if cv_data:
            # Organize the data for rendering in the template
            cv_info = {
                'name': cv_data[0]['name'],
                'email': cv_data[0]['email'],
                'phone': cv_data[0]['phone'],
                'location': cv_data[0]['location'],
                'education': cv_data[0]['education'],
                'skills': cv_data[0]['skills'].split(', '),  # Split skills into a list
                'experience': cv_data[0]['experience'].split('\n'),  # Split experience into a list
                'projects': cv_data[0]['projects'].split('\n'),  # Split projects into a list
                'github': cv_data[0]['github'],
            }

            return render_template('cv.html', cv_info=cv_info)
        else:
            return render_template('cv.html', cv_info=None)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return "An error occurred. Please check the logs for details."

if __name__ == '__main__':
    app.run(debug=True)
