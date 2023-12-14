from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from DB.database import Base
from datetime import datetime

class Employee(Base):
    __tablename__ = 'employee'
    __table_args__ = {'schema': 'useraccessmgmt'}

    Employee_ID = Column(Integer, primary_key=True, autoincrement=True)
    F_Name = Column(String(25), nullable=False)
    L_Name = Column(String(35), nullable=False)
    Email = Column(String(45), nullable=True)
    Phone = Column(String(14), nullable=True)



class Role(Base):
    __tablename__ = 'role'
    __table_args__ = {'schema': 'useraccessmgmt'}

    Role_ID = Column(Integer, primary_key=True, autoincrement=True)
    Role_Name = Column(String(45), nullable=True)
    Role_Description = Column(String(200), nullable=False)


class Permission(Base):
    __tablename__ = 'permission'
    __table_args__ = {'schema': 'useraccessmgmt'}

    Permission_ID = Column(Integer, primary_key=True, autoincrement=True)
    Permission_Name = Column(String(45), nullable=False)
    Permission_Description = Column(String(45), nullable=True)


class Application(Base):
    __tablename__ = 'application'
    __table_args__ = {'schema': 'useraccessmgmt'}

    Application_ID = Column(Integer, primary_key=True, autoincrement=True)
    Application_Name = Column(String(45), nullable=False)
    Application_Description = Column(String(200), nullable=True)


class Employee_Role(Base):
    __tablename__ = 'employee_role'
    __table_args__ = {'schema': 'useraccessmgmt'}

    Employee_ID = Column(Integer, ForeignKey('employee.Employee_ID'), primary_key=True)
    Role_ID = Column(Integer, ForeignKey('role.Role_ID'), primary_key=True)
    Application_ID = Column(Integer, ForeignKey('application.Application_ID'), primary_key=True)
    Role_Assigned_Date = Column(DateTime, nullable=False)
    Role_Revoked_Date = Column(DateTime, nullable=True)



class Employee_Application(Base):
    __tablename__ = 'employee_application'
    __table_args__ = {'schema': 'useraccessmgmt'}

    Employee_Application_ID = Column(Integer, primary_key=True, autoincrement=True)
    Employee_ID = Column(Integer, ForeignKey('employee.Employee_ID'), nullable=False)
    Application_ID = Column(Integer, ForeignKey('application.Application_ID'), nullable=False)
    Application_Assigned_Date = Column(DateTime, nullable=False)
    Application_Revoked_Date = Column(DateTime, nullable=True)



class Application_Role(Base):
    __tablename__ = 'application_role'
    __table_args__ = {'schema': 'useraccessmgmt'}

    Application_Role_ID = Column(Integer, primary_key=True, autoincrement=True)
    Role_ID = Column(Integer, ForeignKey('role.Role_ID'), nullable=False)
    Application_Name = Column(String(45), nullable=False)
    Application_Description = Column(String(45), nullable=True)



class Role_Permission(Base):
    __tablename__ = 'role_permission'
    __table_args__ = {'schema': 'useraccessmgmt'}

    Role_Permission_ID = Column(Integer, primary_key=True, autoincrement=True)
    Role_ID = Column(Integer, ForeignKey('role.Role_ID'), nullable=False)
    Permission_ID = Column(Integer, ForeignKey('permission.Permission_ID'), nullable=False)
    Role_Permission_Description = Column(String(45), nullable=True)



class Audit(Base):
    __tablename__ = 'audit'
    __table_args__ = {'schema': 'useraccessmgmt'}

    Audit_ID = Column(Integer, primary_key=True, autoincrement=True)
    Employee_ID = Column(Integer, ForeignKey('employee.Employee_ID'), nullable=False)
    Application_ID = Column(Integer, ForeignKey('application.Application_ID'), nullable=False)
    Role_ID = Column(Integer, ForeignKey('role.Role_ID'), nullable=False)
    Permission_ID = Column(Integer, ForeignKey('permission.Permission_ID'), nullable=False)
    Action_Type = Column(String(45), nullable=False)
    Action_Date = Column(DateTime, nullable=False)
    Action_Details = Column(String(45), nullable=True)

