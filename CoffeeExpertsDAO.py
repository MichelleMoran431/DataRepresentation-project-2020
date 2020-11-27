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

    def create(self,coffeeconsumer):    
        cursor = self.db.cursor()
        sql="insert into coffeeconsumers (firstname,lastname,postcode) values (%s,%s,%s)"
        values = [
            coffeeconsumer['firstname'],
            coffeeconsumer['lastname'],
            coffeeconsumer['postcode']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

        #make a new instance of the class to get the code to run
#coffeedao = coffeedao()

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from coffeeconsumers"
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

    def update(self,coffeeconsumer):
        cursor = self.db.cursor()
        sql = " update coffeeconsumers set firstname = %s, lastname = %s,postcode = %s where id = %s"
        values =[   
            coffeeconsumer['id'],
            coffeeconsumer['firstname'],
            coffeeconsumer['lastname'],
            coffeeconsumer['postcode']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return coffeeconsumer

    def delete (self,id):
        cursor = self.db.cursor()
        sql='delete  from coffeeconsumers where id = %s'
        values =[id]
        cursor.execute(sql,values)
        return{}

    #create a function to convert results to dict for later use in html file
    def convertToDict (self,result):
        colnames = ['id','firstname','lastname','postcode']
        coffeeconsumer={} # create a tuple

        if result:
            for i,colName in enumerate(colnames):
                value = result[i]
                coffeeconsumer[colName]=value
            return coffeeconsumer
    
coffeedao = coffeedao()  