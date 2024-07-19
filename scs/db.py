import mysql.connector

class DB:
    def connectToDatabase(self):
        try:
            self.db = mysql.connector.connect(
            host='localhost',user='Aryaman',password='Arya@123',database='miniproject'
            )
            self.dbcursor = self.db.cursor()
            self.db.autocommit = True

            print("Connected to Database Successfully")

            return self.dbcursor

        except Exception as e:
            print("Error connecting to database")
            print(e)
            quit(-1)
            
    def __init__(self):
        self.connectToDatabase()