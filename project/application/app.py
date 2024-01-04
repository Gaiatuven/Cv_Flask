import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get the absolute path to the data directory (relative to the script)
data_directory = os.path.join(os.path.dirname(__file__), 'data')

# Ensure the data directory exists
os.makedirs(data_directory, exist_ok=True)

# Set the SQLite database URI (consistent with the data directory path)
database_path = os.path.join(data_directory, 'cv_database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
