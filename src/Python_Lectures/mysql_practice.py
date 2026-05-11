import loguru
import mysql.connector
from loguru import *

connection = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="Doglasdc3*")

logger.info(f"{connection}")

cursor=connection.cursor()
cursor.execute("select * from emp_db.car")

result=cursor.fetchall()
logger.info(f"{result}")