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
    p1 = Person("44","ali44","lot44") 
    print p1.getName()
    p1.toString()
    personDao = PersonDao()
    personDao.insertPerson(p1)
    #connect()
    # app.run()
    
