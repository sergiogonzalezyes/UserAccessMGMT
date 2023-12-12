from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Numeric, Float
from sqlalchemy.orm import relationship
from DB.database import Base, engine
from datetime import datetime



class Employee(Base):
    __tablename__ = 'employee'

    Employee_ID = Column(Integer, primary_key=True, autoincrement=True)
    F_Name = Column(String(25), nullable=False)
    L_Name = Column(String(35), nullable=False)
    Email = Column(String(45), nullable=True)
    Phone = Column(String(14), nullable=True)


class Role(Base):
    __tablename__ = 'role'

    Role_ID = Column(Integer, primary_key=True, autoincrement=True)
    Role_Name = Column(String(45), nullable=True)
    Role_Description = Column(String(45), nullable=False)


class Permission(Base):
    __tablename__ = 'permission'

    Permission_ID = Column(Integer, primary_key=True, autoincrement=True)
    Permission_Name = Column(String(45), nullable=False)
    Permission_Description = Column(String(45), nullable=True)



class Application(Base):
    __tablename__ = 'application'

    Application_ID = Column(Integer, primary_key=True, autoincrement=True)
    Application_Name = Column(String(45), nullable=False)
    Application_Description = Column(String(45), nullable=True)



class Employee_Role(Base):
    __tablename__ = 'employee_role'

    Employee_ID = Column(Integer, primary_key=True, autoincrement=True)
    Role_ID = Column(Integer, ForeignKey=('Role'), nullable=False)
    Application_ID = Column(Integer, ForeignKey=('Application'), nullable=False)
    Role_Assigned_Date = Column(DateTime, nullable=False)
    Role_Revoked_Date = Column(DateTime, nullable=True)


class Employee_Application(Base):
    __tablename__ = 'employee_application'

    Employee_ID = Column(Integer, primary_key=True, autoincrement=True)
    Application_ID = Column(Integer, ForeignKey=('Application'), nullable=False)
    Application_Assigned_Date = Column(DateTime, nullable=False)
    Application_Revoked_Date = Column(DateTime, nullable=True)


class Application_Role(Base):
    __tablename__ = 'application_role'

    Application_ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Role_ID = Column(Integer, ForeignKey=('Role'), nullable=False)
    Application_Name = Column(String(45), nullable=False)
    Application_Description = Column(String(45), nullable=True)



class Role_Permission(Base):
    __tablename__ = 'role_permission'

    Role_ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Permission_ID = Column(Integer, ForeignKey=('Permission'), nullable=False)
    Role_Permission_Description = Column(String(45), nullable=True)



class Audit(Base):
    __tablename__ = 'audit'

    Audit_ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Employee_ID = Column(Integer, ForeignKey=('Employee'), nullable=False)
    Application_ID = Column(Integer, ForeignKey=('Application'), nullable=False)
    Role_ID = Column(Integer, ForeignKey=('Role'), nullable=False)
    Permission_ID = Column(Integer, ForeignKey=('Permission'), nullable=False)
    Action_Type = Column(String(45), nullable=False)
    Action_Date = Column(DateTime, nullable=False)
    Action_Details = Column(String(45), nullable=True)