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
        except Error as ex:
             print(ex)

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

    def checkUser(self,id):
        conn = self.connect()
        if (conn is not None ):
            queryString = "SELECT count(id) FROM person WHERE id = '%s'" 
            cursor = conn.cursor(buffered=True)
            cursor.execute(queryString,id)
            #numrow = int(cursor.rowcount)
            numrow = cursor.fetchone()
            print "show numbers"
            print numrow
        self.commit()
        self.closeConnection()
        if (numrow[0] > 0 ):
            return True
        else:
            return False

    
