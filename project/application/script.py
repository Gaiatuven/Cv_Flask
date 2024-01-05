import sqlite3

def fetch_cv_data(database_path):
    # Correctly connect to the database using the constructed path
    conn = sqlite3.connect(database_path)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    try:
        # Define the SQL command to select information from the table
        select_query = '''
        SELECT name, email, phone, location, education, skills, experience, projects, github
        FROM cv_data;
        '''

        # Execute the SQL command
        cursor.execute(select_query)

        # Fetch all the results as a list of dictionaries
        results = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        cv_data = [dict(zip(columns, row)) for row in results]

        return cv_data

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        # Close the connection
        conn.close()

# Example usage
database_path = 'project/application/data/cv_database.db'
cv_data = fetch_cv_data(database_path)
for entry in cv_data:
    print(entry)
