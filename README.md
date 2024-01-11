# Flask CV Application

This is a simple Flask web application for managing and displaying CV information. The application uses Flask, SQLAlchemy, and Jinja for rendering templates.

## Features

- Display personal information, education, skills, experience, projects, and GitHub information.
- SQLite database for data storage.
- Basic error handling.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-flask-cv-app.git
    cd your-flask-cv-app
    ```

2. Create a virtual environment:

    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:

    - On Linux/macOS:

        ```bash
        source env/bin/activate
        ```

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:

    ```bash
    python app.py
    ```

    The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

## Project Structure

- `app.py`: The main Flask application file.
- `script.py`: Contains functions for fetching CV data.
- `templates/`: HTML templates for rendering pages.
- `static/`: Static files such as CSS, images, etc.
- `data/`: Directory for storing the SQLite database.

## Contributing

If you find a bug, have questions, or want to contribute, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
