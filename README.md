# Expense Tracker

An expense tracking web application built using Flask and SQLAlchemy that allows users to add, view, and manage their expenses.

## Features

- Add new expenses with a description and category.
- View a list of all expenses.
- Manage and track expenses with a user-friendly interface.

## Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML, CSS
- **Database**: SQLite (or upgradeable to other databases such as PostgreSQL or MySQL)
  
## Setup Instructions

### Prerequisites

- Python 3.x
- Git
- Virtualenv (optional, but recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jithinjithu10/Expense-Tracker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Expense-Tracker
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Set up environment variables (if needed):

    Create a `.env` file and add the following:
    ```env
    FLASK_APP=app
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    ```

7. Initialize the database:

    ```bash
    flask shell
    from app import db
    db.create_all()
    exit()
    ```

8. Run the application:

    ```bash
    flask run
    ```

The application will be available at `http://127.0.0.1:5000/`.

## Project Structure

```
Expense-Tracker/
│
├── app/
│   ├── __init__.py        # Initializes the Flask app and database
│   ├── models.py          # Defines database models
│   ├── routes.py          # Application routes (views)
│   ├── static/            # Static files (CSS, images, etc.)
│   └── templates/         # HTML templates
│
├── venv/                  # Virtual environment (if created locally)
├── requirements.txt       # List of dependencies
├── .gitignore             # Ignored files and folders for git
└── README.md              # This file
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m 'Add my feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
