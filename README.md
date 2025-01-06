# CRUD API with Flask and SQLite

## Overview
This project implements a simple CRUD (Create, Read, Update, Delete) API using Flask and SQLite for managing users. The users are stored in an SQLite database, and the API supports basic operations for creating, retrieving, updating, and deleting user data.

## API Endpoints
To interact with the API, you can use the following `curl` commands.
To create a new user by providing `email`, `username`, and `birthday`:
```
curl -X POST http://127.0.0.1:5000/create_user -H "Content-Type: application/json" -d "{\"email\": \"newuser@example.com\", \"username\": \"newuser\", \"birthday\": \"1990-01-01\"}"
To retrieve the information of a user by their ID (replace 1 with the desired user ID):

curl -X GET http://127.0.0.1:5000/get_user/1
To update a user's information (email, username, birthday) based on their ID:

curl -X PUT http://127.0.0.1:5000/update_user/1 -H "Content-Type: application/json" -d "{\"email\": \"updateduser@example.com\", \"username\": \"updateduser\", \"birthday\": \"1991-01-01\"}"
To delete a user based on their ID:

curl -X DELETE http://127.0.0.1:5000/delete_user/1
```
## Project Setup
### Requirements
- Python 3.x
- Flask
- SQLite
Installation
Clone the repository:
```
git clone https://github.com/mylovenkt/simple-crud-api.git
cd simple-crud-api
```
Install the required dependencies:
```
pip install -r requirements.txt
```
Run the Flask server:
```
python app.py
```
The server should now be running at http://127.0.0.1:5000/. You can use the provided curl commands to interact with the API.
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
