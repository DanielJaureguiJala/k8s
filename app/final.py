from flask import Flask
from flask import request
import mysql.connector
# pip install mysql-connector-python
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return """<center><h1><p>Final Project - k8s!</p></h1></center>
    <pre>
    <strong><h2>Store Endpoint</h2></strong>
    Send a Post request to "store" endpoint with specific body to save data in the mysql database.
    
    <strong>Method:</strong> POST
    <strong>endpoint:</strong> store
    <strong>Body Json:</strong>
    {
        "Name": "Daniel",
        "LastName": "Jauregui",
        "Role": "QA Automation Engineer"
    }
    
    <strong><h2>List Endpoint</h2></strong>
    Send a Get request to "list" endpoint to see all data stored in mysql.
    
    <strong>Method:</strong> GET
    <strong>endpoint:</strong> list    
    </pre>"""


@app.route("/store", methods=['POST'])
def store():
    conn = self.__connect_to_db()
    sqlConn = conn.cursor()
    sql = "INSERT INTO users (name, last, role) VALUES (%s, %s, %s)"
    user_info = request.get_json()
    name = str(user_info.get('Name')).encode("utf-8")
    last = str(user_info.get('LastName')).encode("utf-8")
    role = str(user_info.get('Role')).encode("utf-8")
    val = (name, last, role)
    sqlConn.execute(sql, val)
    conn.commit()
    return f" {conn.rowcount} record inserted."


@app.route("/list", methods=['GET'])
def list():
    start_table = """
    <center>
    <table border="1" cellpadding="1" cellspacing="1" style="width:630px">
    <tbody>
    <tr>
    <td style="text-align:center; width:42px"><strong>#</strong></td>
    <td style="text-align:center; width:163px"><strong>Name</strong></td>
    <td style="text-align:center; width:190px"><strong>Last Name</strong></td>
    <td style="text-align:center; width:208px"><strong>Role</strong></td>
    </tr>
    """
    end_table = """
    </tbody>
    </table>
    </center>
    """

    conn = self.__connect_to_db()
    sqlConn = conn.cursor()
    sql = "select * from users"
    results = sqlConn.execute(sql)
    conn.commit()
    rows = ""
    number = 1
    for result in results:
        rows = f"""
        <tr>
        <td style="width:42px">{number}</td>
        <td style="width:163px">{result.get('name')}</td>
        <td style="width:190px">{result.get('last')}</td>
        <td style="width:208px">{result.get('role')}</td>
        </tr>
        """
        number += 1
    return start_table + rows + end_table


def __connect_to_db():
    conn = mysql.connector.connect(
        host="mysql-svc",
        user="root",
        password="root",
        database="myappdb"
    )
    return conn
