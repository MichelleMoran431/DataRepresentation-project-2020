import mysql.connector
import DBconfig as cfg

db=mysql.connector.connect(
    host=cfg.mysql['host'],
    username=cfg.mysql['username'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor=db.cursor()
sql="select*from coffeeconsumers"

cursor.execute(sql)
result=cursor.fetchall()
for x in result:
    print(x)