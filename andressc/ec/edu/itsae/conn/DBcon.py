'''
Created on 19/2/2015

@author: PC29
'''

from flaskext.mysql import MySQL
from flask import Flask


class DBcon(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        pass
    
    def conexion(self):
        mysql = MySQL()
        app = Flask(__name__)
        app.config['MYSQL_DATABASE_USER'] = 'python1'
        app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
        app.config['MYSQL_DATABASE_DB'] = 'ventas1'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)
        
        return mysql
