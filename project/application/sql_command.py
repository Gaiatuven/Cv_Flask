import sqlite3
import os

# Get the path to the data directory relative to the script's location
data_directory = os.path.join(os.path.dirname(__file__), 'data')

# Ensure the data directory exists
os.makedirs(data_directory, exist_ok=True)

database_path = os.path.join(data_directory, 'cv_database.db')

# Correctly connect to the database using the constructed path
conn = sqlite3.connect(database_path)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL command to create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS cv_data (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,       -- Add phone column
    location TEXT,    -- Add location column
    education TEXT,   -- Add education column
    skills TEXT,
    experience TEXT,
    projects TEXT,
    github TEXT       -- Add github column
);
'''

# Execute the SQL command to create the table
cursor.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Insert CV information into the table
insert_cv_query = '''
INSERT INTO cv_data (name, email, phone, location, education, skills, experience, projects, github)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
'''

cv_info = (
    'Gregory Claassen',
    'ggwiese@gmail.com',
    '+27734644578',
    'Cape Town South Africa',
    'NDiploma in Marketing Management - University of South Africa (UNISA) (2009), National Certificate N4-N6 in Marketing Management from Northlink College (2006 - 2008), Basic Computer Literacy Certificate from Office Administration (2009), ICDL (International Computer Driver’s License) Certificate from Northlink College (2009)',
    'HTML5, CSS3, Python, Streamlit, Flask, PostgreSQL',
    'Administration Specialist - Old Mutual Claims and Underwriting (2010 - Current)\n\nKey Responsibilities:\n- Managed and tracked various daily administrative tasks across departments, including:\n    - Medical coding\n    - Customer reassurance\n    - Medical investigations\n    - Auditing\n- Maintained accurate and up-to-date spreadsheets (MIS) for efficient data management.\n- Handled web recall activities, ensuring compliance with enquiry categories and acceptance of terms.\n- Provided coaching and training for staff on Greenlight / OMP product and process knowledge, empowering them to work independently and deliver excellent service.\n- Offered empathetic and efficient inbound phone line support for intermediaries via telephonic contact model, exceeding customer satisfaction expectations.',
    '2020-01-01 to 2022-12-31: Project ABC - Managed and executed a successful project, achieving XYZ results.',
    'https://github.com/Gaiatuven'
)

cursor.execute(insert_cv_query, cv_info)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
