# Lost & Found

## Overview

Lost & Found is a web application designed to help guardians find their lost children using face recognition technology. The application allows guardians to register their child's information and photo, and if a child is found by someone, their details can be matched against the database to identify and reunite them with their guardians.

## Features

- **User Authentication**: Users can sign up and log in to the application.
- **Guardian Form**: Guardians can register their child's information and upload a photo.
- **Unknown Form**: People who find lost children can submit their details and photo for matching.
- **Face Recognition**: The application uses face recognition to match the found child's photo with the registered children's photos.
- **Status Check**: Guardians can check the status of their registered child.
- **Image Retrieval**: Retrieve the image of the matched child.

## Technology Stack

- **Frontend**: HTML, Bootstrap
- **Backend**: Python, Flask
- **Database**: SQLAlchemy (SQLite)
- **Face Recognition**: face_recognition library

## Directory Structure

```
Lost-Found/
├── images/               # Directory for storing images
├── website/              # Main application directory
│   ├── templates/        # HTML templates
│   │   ├── base.html
│   │   ├── guardianForm.html
│   │   ├── unknownForm.html
│   │   ├── login.html
│   │   └── ...
│   ├── __init__.py       # Flask application setup
│   ├── auth.py           # Authentication routes
│   ├── models.py         # Database models
│   ├── views.py          # Main application routes
│   └── ...
├── main.py               # Entry point for the application
├── requirements.txt      # Python dependencies
└── ...
```

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- face_recognition
- SQLAlchemy

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/sahilsasane/Lost-Found.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Lost-Found
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```sh
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

### Running the Application

1. Run the Flask development server:
   ```sh
   flask run
   ```
2. Open your web browser and visit `http://127.0.0.1:5000/`.

### Usage

1. **Sign Up**: Create a new account.
2. **Log In**: Log in with your credentials.
3. **Register Child**: Fill out the guardian form to register your child's information.
4. **Submit Found Child**: Fill out the unknown form if you find a lost child.
5. **Check Status**: Check the status of your registered child.

## License

This project is licensed under the MIT License.
