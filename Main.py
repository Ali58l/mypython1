#!/usr/bin/python
from flask import Flask, url_for
import mysql.connector
from Person import Person
from PersonDao import PersonDao
from mysql.connector import Error
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome Ali\n'

# @app.route('/articles')
# def api_articles():
#     return 'List of ' + url_for('api_articles')

# @app.route('/articles/<articleid>')
# def api_article(articleid):
#     return 'You are reading ' + articleid

if __name__ == '__main__':
    id = raw_input("Enter username::")
    personDao = PersonDao()
    userExist = personDao.checkUser(id)
    print userExist
    if (not userExist):
        p1 = Person(id,"ali"+ id,"lot"+id) 
        personDao.insertPerson(p1)
    else:
        print "user:: " + id  + " already exist!"
    #connect()
    # app.run()
    
