from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from sqlalchemy.orm import sessionmaker
from DB.database import engine
#from DB.classes import CLASSES GO HERE


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "https://localhost:8080"}}, methods={['GET', 'POST', 'PUT', 'DELETE']})

Session = sessionmaker(bind=engine)

app.route('/')
def hello():
    try:
        print('hellooo')
        session = Session()
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        session.close()