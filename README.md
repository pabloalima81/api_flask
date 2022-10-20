# API Flask - Risk Index

To run a DB docker container.

Create DB docker image
`docker build -t risk_index_db .`

Run Docker DB
`docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=risk_index -e MYSQL_USER=mysql -e MYSQL_PASSWORD=mysql risk_index_db`

Create Virtual Env
`python3 -m venv venv`

Execute Venv
`source venv/bin/activate`

RUN `pip3 install --upgrade pip` update PIP
RUN `pip3 --no-cache-dir install -r requirements.txt` Install requirements.txt

RUN `python3 app.py`

Employee score
http://127.0.0.1:5000/employeescore/rickeyguerrero

Department Score
http://127.0.0.1:5000/departmentscore/4132
