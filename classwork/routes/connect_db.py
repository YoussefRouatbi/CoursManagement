import mysql.connector
def connect_database():
    return mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coursemanagement',port=3307)

if '__main__' == __name__:
    connect_database()
