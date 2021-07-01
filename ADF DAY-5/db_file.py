import mysql.connector
from configparser import ConfigParser

file= "config.ini"
config=ConfigParser()
config.read(file)

mydb = mysql.connector.connect(
    host = "localhost",
    user = config['database']['user_name'],
    password = config['database']['password_pwd'],
    database = config['database']['database_name']
)

print("Database Connection successfull") if (mydb) else  print("Database Not Connected")

mycursor = mydb.cursor()
mycursor= mydb.cursor(buffered=True)

