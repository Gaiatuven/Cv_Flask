import sqlite3
import os

# Get the path to the data directory relative to the script's location
data_directory = os.path.join(os.path.dirname(__file__), '../data')

# Ensure the data directory exists
os.makedirs(data_directory, exist_ok=True)

database_path = os.path.join(data_directory, 'cv_database.db')

# Correctly connect to the database using the constructed path
conn = sqlite3.connect(database_path)  # Corrected path usage

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL command to create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS cv_data (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    profile_summary TEXT,
    skills TEXT,
    experience TEXT,
    projects TEXT
);
'''

# Execute the SQL command to create the table
cursor.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Insert CV information into the table
insert_cv_query = '''
INSERT INTO cv_data (name, email, profile_summary, skills, experience, projects)
VALUES (?, ?, ?, ?, ?, ?);
'''

cv_info = (
    'Gregory Claassen',
    'ggwiese@gmail.com', 
    'Dedicated and resourceful Administration professional with 13 years of experience driving operational excellence. Skilled in training and empowering teams, optimizing telephony systems like Avaya, and ensuring accurate medical coding in healthcare settings. Passionate about exceeding customer expectations through prompt and efficient service. Enthusiastic about applying skills and experience in a Cloud industry.',
    'HTML5, CSS3, Python, Streamlit, Flask, PostgreSQL',
    'Telephony Agent - Edcon (2009 - 2010): Customer services, Debt Collection, New Accounts, Call Centre. Administration Specialist - Old Mutual Claims and Underwriting - (2010 - Current): Managed and tracked various daily administrative tasks across departments, including medical coding, customer reassurance, medical investigations, and auditing. Maintained accurate and up-to-date spreadsheets (MIS) for efficient data management. Handled web recall activities and ensured compliance with enquiry categories and acceptance of terms. Provided coaching and training for staff on Greenlight / OMP product and process knowledge, empowering them to work independently and deliver excellent service. Offered empathetic and efficient inbound phone line support for intermediaries via telephonic contact model, exceeding customer satisfaction expectations.',
    ''  # Add an empty string for the projects field
)


cursor.execute(insert_cv_query, cv_info)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
