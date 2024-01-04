import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get the absolute path to the script's directory
script_directory = os.path.abspath(os.path.dirname(__file__))

# Set the working directory to the script's directory
os.chdir(script_directory)

# Get the absolute path to the data directory
data_directory = os.path.join(script_directory)

# Ensure the data directory exists
os.makedirs(data_directory, exist_ok=True)

# Set the SQLite database URI to use the data directory
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(data_directory, "cv_database.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)
