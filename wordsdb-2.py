
import mysql.connector
import re

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "49200321",
    database = "vocab"
)

cursor = conn.cursor()

# cursor.execute("CREATE DATABASE vocab")

found = False

cursor.execute("SHOW DATABASES")
found = False

# Check if database: vocab exists; if not exists then create a database
for db in cursor:
    print(db)
    pattern = "[(,')]"
    db_string = re.sub(pattern, "", str(db))
    # print("db_string is: " + db_string)
    if (db_string == 'vocab'):
        found = True
        print("database vocab exists")
if (not found):
    print("im here")
    cursor.execute("CREATE DATABASE vocab")

sql = "DROP TABLE IF EXISTS vocab_table"
cursor.execute(sql)

sql = "CREATE TABLE vocab_table(word VARCHAR(255), definition VARCHAR (255))"
cursor.execute(sql)
fh = open("Vocabulary_list.csv")

wd_list = fh.readlines()

# print(wd_list[0])

wd_list.pop(0)

vocab_list = []

# print(wd_list)

for rawstring in wd_list:
    word, definition = rawstring.split(',', 1)
    definition = definition.rstrip()
    vocab_list.append({word, definition})
    sql = "INSERT INTO vocab_table(word, definition) VALUES(%s, %s)"
    values = (word, definition)
    # print(values)
    cursor.execute(sql, values)

    conn.commit()
    # print( "Inserted " + str(cursor.rowcount)+ "row into vocab_table ")

sql = "SELECT * from vocab_table WHERE word = %s"
value = ['boisterous']
cursor.execute(sql, value)
result = cursor.fetchall()

for row in result:
    print (row)

sql = 'UPDATE vocab_table SET definition = %s WHERE word = %s'
value = ["spirited; lively" , 'boisterous']
cursor.execute(sql, value)

conn.commit()

print("Modified row count: ", cursor.rowcount)

sql = "SELECT * from vocab_table WHERE word = %s"
value = ['spirited']
cursor.execute(sql, value)
result = cursor.fetchall()

for row in result:
    print (row)


# print (vocab_list)