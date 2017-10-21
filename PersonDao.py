from Person import Person
import mysql.connector #import Error
class PersonDao: 
    def __init__(self):
        self.conn = self.connect()
    def connect(self):
       # """ Connect to MySQL database """
        try:
            self.conn = mysql.connector.connect(host='localhost',database='mydb1', user='root', password='123')
            if self.conn.is_connected():
                print('Connected to MySQL database')
                return self.conn
        except Error as e:
             print(e)

    def commit(self):
        self.conn.commit()

    def closeConnection(self):    
        self.conn.close()
 
    def insertPerson(self,person):
        conn = self.connect()
        if (conn is not None ):
            queryString = "INSERT INTO person(id,name,lname) VALUES(%s,%s,%s)"
            cursor = conn.cursor()
            cursor.execute(queryString,(person.id,person.name,person.lname))
        self.commit()
        self.closeConnection()
