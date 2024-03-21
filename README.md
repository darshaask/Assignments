## Flask-RabbitMQ-Celery Integration

This project implements a Flask API endpoint (app.py) and a Celery worker (tasks.py) integrated with RabbitMQ for asynchronous processing.

## Prerequisites
1. Flask
2. RabbitMQ
3. Celery
4. SQLite(Mysql used)

It's recommended to have these prerequisites installed before proceeding with the development.

## Installation and Setup
1.  Install dependencies:

2. Configure database parameters, RabbitMQ exchange, and queue names in the respective configuration files.

## Running the Application
3. Start the Flask application:

4. Start the Celery worker:

## Usage
1. Use the provided Postman collection to test the Flask API endpoints.
2. Send a POST request to the `/api/items` endpoint with JSON data in the format:

To fulfill your requirements, let's break down the tasks and create a checklist:

Task Checklist:
Flask API Endpoint (Producer):

 Create a Flask application with an API endpoint that accepts POST requests.
 Define the endpoint to accept JSON data with an "item" field.
 Insert the received data into the SQLite database with a "pending" status.
 Send the data to RabbitMQ for further processing.
 Return a response with status code 202.
Celery Worker (Consumer):

 Create a Celery worker that consumes messages from RabbitMQ.
 Extract the "item" from the message and update the corresponding row in the database to "completed".
 Ensure the worker handles rows with the same item name properly.
Configuration Files:

 Create separate configuration files for database parameters, RabbitMQ exchange, and queue names.
Postman Collection:

 Create a Postman collection with endpoints for testing the Flask API.
Git Repository (Optional):

 Push all relevant files to a Git repository on GitLab.
Readme File:

 Create a README file with detailed instructions on how to set up and run the project.
 Include a requirements.txt file listing all dependencies.
Readme File:
markdown
Copy code
# Flask-RabbitMQ-Celery Integration

This project implements a Flask API endpoint (Producer) and a Celery worker (Consumer) integrated with RabbitMQ for asynchronous processing.

## Prerequisites
1. Flask
2. RabbitMQ
3. Celery
4. SQLite

It's recommended to have these prerequisites installed before proceeding with the development.

## Installation and Setup
1. Clone the repository:

git clone <repository_url>

markdown
Copy code

2. Install dependencies:

pip install -r requirements.txt

markdown
Copy code

3. Configure database parameters, RabbitMQ exchange, and queue names in the respective configuration files.

## Running the Application
1. Start the Flask application:

python app.py

markdown
Copy code

2. Start the Celery worker:

celery -A tasks worker --loglevel=info

markdown
Copy code

## Usage
1. Use the provided Postman collection to test the Flask API endpoints.
2. Send a POST request to the `/api/items` endpoint with JSON data in the format:
{
"item": "book"
}
   
markdown
Copy code
3. Check the SQLite database to verify the status of the inserted item.

## Files and Directory Structure
- `app.py`: Main Flask application file.
- `tasks.py`: Celery tasks file.
- `celeyconfig.py`: Configuration file for database parameters.
- `requirements.txt`: List of dependencies.
- `postman_collection.json`: Postman collection for testing endpoints.
  (https://solar-water-795829.postman.co/workspace/New-Team-Workspace~c6e5be70-dada-4c64-ab9e-281adbad7853/collection/33610654-8b87e5f8-97eb-4855-bb35-5f28e2acbd8d?action=share&creator=33610654)


