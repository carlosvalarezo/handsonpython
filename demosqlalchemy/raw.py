from sqlalchemy import create_engine

db_string = "postgresql://postgres:postgres@localhost:5432/mydb"

db = create_engine(db_string)

# Create
db.execute('''CREATE TABLE table3(
            id INTEGER PRIMARY KEY,
            completed BOOLEAN NOT NULL DEFAULT False,
            creation_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
          );''')

insert_clause_no_params = 'INSERT INTO table3(id, completed) VALUES (1, true);'
insert_clause_params_1 = 'INSERT INTO table3(id, completed) VALUES (%(id)s, %(completed)s);'

data_1 = {'id': 2, 'completed': False}

db.execute('INSERT INTO table3(id, completed) VALUES (%s, %s);', (4, True))

db.execute(insert_clause_no_params)
db.execute(insert_clause_params_1, data_1)

result_set = db.execute("SELECT * FROM table3")
for r in result_set:
    print(r)

db.execute("UPDATE table3 SET completed=False WHERE id=4")

db.execute("DELETE FROM table3 WHERE id=1")
