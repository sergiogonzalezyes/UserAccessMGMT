from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv()
from DB.database import engine, Base
from DB.classes import Employee, Role, Permission, Application, Employee_Role, Employee_Application, Role_Permission, Application_Role, Audit
from sqlalchemy.orm import sessionmaker




app = Flask(__name__)

CORS(app=app, resources={r"/*": {"origins": "http://localhost:3000"}})

Session = sessionmaker(bind=engine)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})


from flask import jsonify

from flask import jsonify

import pandas as pd
from flask import jsonify

@app.route('/employees', methods=['GET'])
def get_employees():
    session = Session()
    employees = session.query(Employee).all()
    employee_data = []
    for employee in employees:
        employee_data.append({
            'id': employee.Employee_ID,
            'firstName': employee.F_Name,
            'lastName': employee.L_Name,
            'email': employee.Email,
            'phone': employee.Phone,
        })

    return jsonify(employee_data)












if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
