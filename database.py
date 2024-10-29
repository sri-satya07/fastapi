import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Using pymysql to create a connection
conn = pymysql.connect(db='fastapi', user='root', passwd='Satya_123', host='localhost')

# Get a SQLAlchemy engine using the pymysql connection
engine = create_engine("mysql+pymysql://", creator=lambda: conn)

# Create a session local factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a base class for declarative models
Base = declarative_base()













# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base

# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Satya_123@localhost/fastapi"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()