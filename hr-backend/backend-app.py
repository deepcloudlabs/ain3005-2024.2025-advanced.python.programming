"""
Layered Applications:
- Api Layer: Flask
- Application Layer: Pure Python
- Data Access Layer: PyMongo
"""
import json

from flask import Flask, jsonify, request
from flask_cors import CORS
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
socketio = SocketIO(hr_rest_api, cors_allowed_origins="*")
mongo_client = MongoClient('localhost', 27017)
hrdb = mongo_client["hrdb"]
employees_collection = hrdb["employees"]
updatable_fields = ["fullname", "salary", "iban", "fulltime", "department"]


# GET http://localhost:5500/employees/11111111110
@hr_rest_api.route('/hr/api/v1/employees/<identity>', methods=['GET'])
def get_employee_by_identity(identity: str):
    return jsonify(employees_collection.find_one({"identity": identity}, {"_id": False}))


# GET http://localhost:5500/employees?page=0&size=5
@hr_rest_api.route('/hr/api/v1/employees', methods=['GET'])
def get_employees_by_page():
    page = 0 if request.args.get("page") is None else int(request.args.get("page"))
    size = 25 if request.args.get("size") is None else int(request.args.get("size"))
    print(page, size)
    return json.dumps([emp for emp in
                       employees_collection.find(filter={}, projection={"_id": False}, skip=(page * size), limit=size)])


# POST http://localhost:5500/employees
@hr_rest_api.route('/hr/api/v1/employees', methods=['POST'])
def hire_employee():
    employee = request.get_json()
    employees_collection.insert_one(employee)
    socketio.emit("hire", employee)
    return jsonify({"status": "OK"})


def extract_updatable_fields(body, fields):
    updatable_body = {}
    for field in fields:
        if field in body:
            updatable_body[field] = body[field]
    return updatable_body


# PUT http://localhost:5500/employees
@hr_rest_api.route('/hr/api/v1/employees/<identity>', methods=['PUT', 'PATCH'])
def update_employee(identity: str):
    global updatable_fields
    employee = request.get_json()
    employee = extract_updatable_fields(employee, updatable_fields)
    employees_collection.find_one_and_update(
        {"identity": identity},
        {"$set": employee},
        upsert=False
    )
    socketio.emit("update", employee)
    return jsonify({"status": "OK"})


# DELETE http://localhost:5500/employees/11111111110
@hr_rest_api.route('/hr/api/v1/employees/<identity>', methods=['DELETE'])
def fire_employee(identity: str):
    emp = employees_collection.find_one({"identity": identity}, {"_id": False})
    employees_collection.delete_one({"identity": identity})
    socketio.emit("fire", {"identity": identity})
    return jsonify(emp)

cors = CORS(hr_rest_api)
socketio.run(hr_rest_api, debug=True, port=7001)
