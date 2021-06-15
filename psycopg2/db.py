import psycopg2

connection = psycopg2.connect(dbname="mydb", user="postgres", password="postgres", host="localhost", port="5432")

cursor = connection.cursor()

cursor.execute('''DROP TABLE IF EXISTS table2;''')

cursor.execute('''CREATE TABLE table2(
                    id INTEGER PRIMARY KEY,
                    completed BOOLEAN NOT NULL DEFAULT False,
                    creation_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
                  );
               ''')
select_clause = 'SELECT * FROM table2;'

insert_clause_no_params = 'INSERT INTO table2(id, completed) VALUES (1, true);'
insert_clause_params_1 = 'INSERT INTO table2(id, completed) VALUES (%(id)s, %(completed)s);'

data_1 = {'id': 2, 'completed': False}

cursor.execute('INSERT INTO table2(id, completed) VALUES (%s, %s);', (4, True))

cursor.execute(insert_clause_no_params)
cursor.execute(insert_clause_params_1, data_1)

cursor.execute(select_clause)

result = cursor.fetchall()

for r in result:
    print(r)

connection.commit()

cursor.close()
connection.close()
