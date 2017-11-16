from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from app import db
from database import Base

class User(Base):
    
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        
    def __repr__(self):
        return '--- {} ---'.format(self.name)
        
class Device(Base):
    
    __tablename__ = 'Device'

    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(120))
    IP = db.Column(db.String(120))
    OS = db.Column(db.String(120))

    def __init__(self, hostname=None, IP=None, OS=None):
        self.hostname = hostname
        self.IP = IP
        self.OS = OS
        self.username = 'afourmy'
        self.password = 'welcome59'
        
    def __repr__(self):
        return self.IP

    # used for querying the database based on the __repr__ of a device
    @property
    def device(self):
        return str(self)

class Department(Base):
    
    __tablename__ = 'departments'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    def __init__(self, name):
        self.name = name


class Employee(Base):
    
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

    def __init__(self, name, department_id):
        self.name = name
        self.department_id = department_id
