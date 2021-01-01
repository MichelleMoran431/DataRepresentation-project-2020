import mysql.connector
from mysql.connector import cursor


class coffeedao:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="coffeeexpress"
    )
        #print ("connection made")

    def create(self,coffeeconsumers):    
        cursor = self.db.cursor()

        #query for one table
        sql="insert into coffeeconsumers (Firstname,Lastname,Postcode,Ordertype) values (%s,%s,%s,%s)"
        #sql code to query two tables with an inner join statement
        #sql= "SELECT coffeeconsumers.id, coffeeconsumers.firstName, coffeeconsumers.lastName, coffeeconsumers.postcode, consumerorders.ordertype FROM consumerorders INNER JOIN coffeeconsumers ON consumerorders.ordertype=coffeeconsumers.ordertype"

        values = [
            #coffeeconsumers['id'],
            coffeeconsumers['Firstname'],
            coffeeconsumers['Lastname'],
            coffeeconsumers['Postcode'],
            coffeeconsumers['Ordertype'],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

        #make a new instance of the class to get the code to run
        #coffeedao = coffeedao()

    def getAll(self):
        cursor = self.db.cursor()
        #sql="select * from coffeeconsumers"
        sql = "SELECT coffeeconsumers.id, coffeeconsumers.firstName, coffeeconsumers.lastName, coffeeconsumers.postcode, consumerorders.ordertype FROM consumerorders INNER JOIN coffeeconsumers ON consumerorders.ordertype=coffeeconsumers.ordertype"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        #want results to be in JSON format
        for result in results:
            resultasDict=self.convertToDict(result)
            returnArray.append(resultasDict)

        return returnArray #return an array of dict objects

    def findById(self,id):
        cursor = self.db.cursor()
        sql="select * from coffeeconsumers where id = %s"
        values =[id]
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self,coffeeconsumers):
        cursor = self.db.cursor()
        sql = " update coffeeconsumers set Firstname = %s, Lastname = %s,Postcode = %s,ordertype = %s, where id = %s"
        values =[   
            coffeeconsumers['id'],
            coffeeconsumers['Firstname'],
            coffeeconsumers['Lastname'],
            coffeeconsumers['Postcode'],
            coffeeconsumers['Ordertype'],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return coffeeconsumers

    def delete (self,id):
        cursor = self.db.cursor()
        sql='delete  from coffeeconsumers where id = %s'
        values =[id]
        cursor.execute(sql,values)
        return{}

    #create a function to convert results to dict for later use in html file
    def convertToDict (self,result):
        colnames = ['id','Firstname','Lastname','Postcode','Ordertype']
        coffeeconsumer={} # create a tuple

        if result:
            for i,colName in enumerate(colnames):
                value = result[i]
                coffeeconsumer[colName]=value
            return coffeeconsumer
    
coffeedao = coffeedao() 
