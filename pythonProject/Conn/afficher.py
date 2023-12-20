from sqlalchemy import text
from urllib.parse import quote_plus
from conn import ENGINE, cursor

query = text("select * from user;")
results = cursor.execute(query)

for row in results:
    print('name : {}'.format(row[1]))
    print('age : {}'.format(row[2]))
