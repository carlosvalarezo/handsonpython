from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_string = "postgresql://postgres:postgres@localhost:5432/mydb"

db = create_engine(db_string)
Base = declarative_base()
