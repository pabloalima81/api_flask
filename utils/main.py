import pandas as pd

def User_score(user_name):

    #Upload files
    function = pd.read_csv (r'utils/functions.csv')
    application = pd.read_csv (r'utils/applications.csv')
    index = pd.read_csv (r'utils/index.csv')

    role_name = function.loc[function.username == user_name,'role_name']
    role_id = function.loc[function.username == user_name,'role_id']
    app_id = application.loc[application.role_id == role_id.iloc[0],'app_id']
    app_score = index.loc[index.role_name == role_name.iloc[0],['score','app_id']]
    score = app_score.loc[app_score.app_id == app_id.iloc[0],'score']
    return (score.iloc[0])

def Department_score(department_code):

    employees = pd.read_csv(r'utils/employees.csv')

    users = employees.loc[employees.department_code==department_code,'username']
    department_score = 0
    for user in users:
        score = int(User_score(user))
        department_score = department_score + score
    return(department_score)
