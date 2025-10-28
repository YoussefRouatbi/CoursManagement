import mysql.connector
def connect_database():
    return mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coursemanagement')

if '__main__' == __name__:
    connect_database()
