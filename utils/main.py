import pandas as pd
import mysql.connector
from mysql.connector import Error

def User_score(user_name):
    db = mysql.connector.connect(
                            host="localhost",
                            user="mysql",
                            password="mysql",
                            database="risk_index"
                            )
    cur = db.cursor()
    cur.execute('SELECT * FROM score')
    df_score = pd.DataFrame(cur.fetchall())
    df_score.columns=['score_id', 'role_name','app_id','score']
    cur.execute('SELECT * FROM functions')
    df_functions = pd.DataFrame(cur.fetchall())
    df_functions.columns=['role_id', 'role_name','username']
    cur.execute('SELECT * FROM applications')
    df_applications = pd.DataFrame(cur.fetchall())
    df_applications.columns=['app_id', 'app_name','role_id','is_critical']

    #Data upload
    function = df_functions #pd.read_csv (r'utils/functions.csv')
    application = df_applications #pd.read_csv (r'utils/applications.csv')
    index = df_score #pd.read_csv (r'utils/index.csv')

    role_name = function.loc[function.username == user_name,'role_name']
    role_id = function.loc[function.username == user_name,'role_id']
    app_id = application.loc[application.role_id == role_id.iloc[0],'app_id']
    app_score = index.loc[index.role_name == role_name.iloc[0],['score','app_id']]
    score = app_score.loc[app_score.app_id == app_id.iloc[0],'score']
    return (score.iloc[0])

def Department_score(department_code):
    db = mysql.connector.connect(
                            host="localhost",
                            user="mysql",
                            password="mysql",
                            database="risk_index"
                            )
    cur = db.cursor()
    cur.execute('SELECT * FROM employees')
    df_employees = pd.DataFrame(cur.fetchall())
    df_employees.columns=['id', 'full_name','div_cod','division','status','country_id','country','department_code','department','date_in','date_out','username','email']

    employees = df_employees #pd.read_csv(r'utils/employees.csv')

    users = employees.loc[employees.department_code==department_code,'username']
    department_score = 0
    for user in users:
        score = int(User_score(user))
        department_score = department_score + score
    return(department_score)