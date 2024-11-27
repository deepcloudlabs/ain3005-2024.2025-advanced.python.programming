"""
Layered Applications:
- Api Layer: Flask
- Application Layer: Pure Python
- Data Access Layer: PyMongo
"""
from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from pymongo import MongoClient

"""
REST over HTTP
State -> Resource -> Database -> Entity
Create a new Resource -> http POST request
             json                  body      -> Database
             
Query a Resource -> http GET request -> Database
                 <- response
                    body       json
                    
Updating a Resource -> http PUT request -> Database
               json              body                     

Delete a Resource -> http DELETE request -> Database
                  <- response
                    body       json
URI -> URL
https://example.com/customers/11111111110

REST over HTTP
1. URI/URL
2. Http Methods: GET, POST, PUT, PATCH, DELETE
3. Representation: json, xml, csv, ...        
REST over Websocket -> socketio           
"""
hr_rest_api = Flask(__name__)
hr_rest_api.config['DEBUG'] = True
socketio = SocketIO(hr_rest_api)
mongo_client = MongoClient('localhost', 27017)
hrdb = mongo_client["hrdb"]
employees_collection = hrdb["employees"]


# GET http://localhost:5500/employees/11111111110
@hr_rest_api.route('/employees/<identity>', methods=['GET'])
def get_employee_by_identity(identity: str):
    return jsonify(employees_collection.find_one({"identity": identity}, {"_id": False}))

# POST http://localhost:5500/employees
@hr_rest_api.route('/employees', methods=['POST'])
def hire_employee():
    employee = request.get_json()
    employees_collection.insert_one(employee)
    return jsonify({"status": "OK"})


# DELETE http://localhost:5500/employees/11111111110
@hr_rest_api.route('/employees/<identity>', methods=['DELETE'])
def fire_employee(identity: str):
    emp = employees_collection.find_one({"identity": identity}, {"_id": False})
    employees_collection.delete_one({"identity": identity})
    return jsonify(emp)


socketio.run(hr_rest_api, debug=True, port=5500)
