# ECG Analyser Project

This is the repository for the ECG Project, a Django REST Framework application with a SQLite database(for simple use purpose)

## Getting Started

These instructions will guide you in setting up the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

- Docker
- Make (for using the Makefile commands)

### Installing

Follow these steps to get your development environment up and running:

1. **Run the project with Docker*

   Run the following command to start the server:

   ```bash
   make start-env```
   
2. **Run the project in a python env**

    ```bash
    pip install -r requirements.txt
    python manage.py runserver 127.0.0.1:8888

3. You can run the test by with the commands:

    - In a Python env you can run the command 
    ```bash
    python manage.py test```

    - Or you can directly the make command that will run them inside a docker container after running the command `env-start`
    ```bash
    make test

