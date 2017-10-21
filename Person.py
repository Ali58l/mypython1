class Person:
    id = ""
    name = ""
    lname = ""

    def __init__(self,id,name,lname):
        self.id = id
        self.name = name
        self.lname = lname
    
    def setNamese(self,name):
        self.name=name
        
    def getName(self):
        return self.name    
    def toString(self):
        print self.id + ", " + self.name  + ", " + self.lname
