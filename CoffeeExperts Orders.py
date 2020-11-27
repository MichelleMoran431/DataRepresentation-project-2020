import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  
  database="coffeeexpress"
)

#cursor = db.cursor()
#sql="CREATE TABLE CoffeeExpert Orders (orderno int NOT NULL AUTO_INCREMENT, id int NOT NULL AUTO_INCREMENT PRIMARY KEY, Order type VARCHAR(255), Order date INT)"

#cursor.execute(sql)
cursor = db.cursor()
cursor.execute("CREATE TABLE customers (id int , orderno INT NOT NULL AUTO_INCREMENT primary key, ordertype VARCHAR(255), orderdate int)")
