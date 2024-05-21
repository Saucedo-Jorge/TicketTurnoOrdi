from flask_mysqldb import MySQL
from App import app

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='ticket'
mysql = MySQL(app)


