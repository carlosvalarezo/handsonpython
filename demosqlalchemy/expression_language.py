import datetime

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, DateTime, Boolean, MetaData

db_string = "postgresql://postgres:postgres@localhost:5432/mydb"

db = create_engine(db_string)

meta = MetaData(db)

table5 = Table('table4', meta,
                   Column('id', Integer, primary_key=True),
                   Column('completed', Boolean),
                   Column('now', DateTime, default=datetime.datetime.now()))

with db.connect() as conn:
    # Create
    table5.create()
    insert_statement_1 = table5.insert().values(id=1, completed=True)
    insert_statement_2 = table5.insert().values(id=2, completed=False)
    insert_statement_3 = table5.insert().values(id=3, completed=True)
    insert_statement_4 = table5.insert().values(id=4, completed=False)

    conn.execute(insert_statement_1)
    conn.execute(insert_statement_2)
    conn.execute(insert_statement_3)
    conn.execute(insert_statement_4)

    # Read
    select_statement = table5.select()
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)

    # Update
    update_statement = table5.update().where(table5.c.id == 1).values(completed=False)
    conn.execute(update_statement)
    select_statement = table5.select()
    result_set = conn.execute(select_statement)
    print("#### after update")
    for r in result_set:
        print(r)

    # Delete
    delete_statement = table5.delete().where(table5.c.id == 1)
    conn.execute(delete_statement)
    select_statement = table5.select()
    result_set = conn.execute(select_statement)
    print("#### after delete")
    for r in result_set:
        print(r)
