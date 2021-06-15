import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Boolean, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgresql://postgres:postgres@localhost:5432/mydb"

db = create_engine(db_string)
base = declarative_base()


class TableSix(base):
    __tablename__ = 'table6'

    id = Column(Integer, primary_key=True)
    completed = Column(Boolean)
    now = Column(DateTime, default=datetime.datetime.now())


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# Create
first_row = TableSix(id=1, completed=True)
second_row = TableSix(id=2, completed=True)
third_row = TableSix(id=3, completed=True)
fourth_row = TableSix(id=4, completed=True)
session.add(first_row)
session.add(second_row)
session.add(third_row)
session.add(fourth_row)

session.commit()

# Read
rows = session.query(TableSix)
for row in rows:
    print(f"{row.id} - {row.completed} - {row.now}")

# Update
first_row.completed = False
session.commit()
print("#### after update")
rows = session.query(TableSix)
for row in rows:
    print(f"{row.id} - {row.completed} - {row.now}")

# Delete
session.delete(first_row)
session.commit()

print("#### after delete")
rows = session.query(TableSix)
for row in rows:
    print(f"{row.id} - {row.completed} - {row.now}")


# base.metadata.drop_all(db, tables=[TableSix.__tablename__])