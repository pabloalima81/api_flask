import pandas as pd
from flask import Flask, jsonify
from utils.main import *


app = Flask(__name__)

@app.route('/')
def index():
    return 'Risk Index API'

@app.route("/employeescore/<string:username>")
def employeescore(username):
    userscore = str(User_score(username))
    return (jsonify(userscore))

@app.route('/departmentscore/<int:department_code>')
def departmentscore(department_code):
    departmentscore = str(Department_score(department_code))
    return (jsonify(departmentscore))

app.run(debug=True)