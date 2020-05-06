# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:00:28 2020

@author: Nitpreet
"""
from flask import Flask , jsonify,request
import mysql.connector
import pymongo
#import json
app = Flask(__name__)
connection = mysql.connector.connect(user = 'root', password = 'nitpreet',host = 'localhost',database = 'test')
connect_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
db_mongo = connect_mongo["test"]
collection = db_mongo["new_collection1"]
@app.route('/create',methods = ['GET','POST'])
def create():
    cursor = connection.cursor()
    if request.method=='POST':
        json_det = request.json
        command = 'Insert into sabudh2(id, name,address,phone_number) VALUES (%s,%s,%s,%s)'
        id = json_det["id"]
        command1 = "Select * from sabudh2 where id = "+str(id)
        cursor.execute(command1)
        rows = cursor.fetchall()
        try:
            if id not in rows:
                    if len(json_det)==4:
                        values = (json_det['id'],json_det['name'],json_det['address'],json_det["phone_number"])
                        cursor.execute(command,values)
                        inp = collection.insert_one(json_det)
                        connection.commit()
                        text = "Id is "+str(id)
                        return jsonify(text)
                    else:
                        return jsonify("Only 4 values allowed")
        except:
            return jsonify("IDNotUnique")
        #ids = {"Mysql ID":cursor.lastrowid,"Mongo ID":inp.inserted_id}
        #json_id = json.dumps(ids)
        #mongo = "Mongo Id is: "+str(inp.inserted_id)
        #mysql = 'Mysql id is: '+str(cursor.lastrowid)
        #return '{}\n{}'.format(mongo,mysql)
@app.route("/update",methods= ['GET','POST'])
def update():
    cursor = connection.cursor()
    if request.method=='POST':
        json = request.json
        id = json['id']
        command1 = "Select * from sabudh2 where id = "+str(id)
        cursor.execute(command1)
        sql_value = []
        for row in cursor:
            sql_value.append(row)
        try:
            name = json['name']
        except:
            name = row[1]
        try:
            phone_number = str(json["phone_number"])
        except:
            phone_number = str(row[3])
        try:
            address = json["address"]    
        except:
            address = row[2]
        command = "Update sabudh2 set name= %s, phone_number = %s, address=%s where id= "+str(id)
        collection.update_one({"id":id},{"$set":{"name":name,"address":address,"phone_number":phone_number}})
        values = (name,phone_number,address)
        cursor.execute(command,values)
        connection.commit()
        
        return jsonify("Updated")
@app.route("/delete",methods= ["GET","POST"])
def delete():
    cursor = connection.cursor()
    if request.method=='POST':
        json = request.json
        if len(json)==1:
            id = json['id']
            command = "DELETE FROM sabudh2 where id = "+str(id)
            cursor.execute(command)
            connection.commit()
            collection.delete_one({"id":id})
            return jsonify("deleted")
        else:
            return jsonify("Only Id is allowed")
@app.route('/detect_prime',methods = ["GET","POST"])
def detect_prime():
    if request.method=="POST":
        json = request.json
        num = json["number"]
        if num>1000000:
            prime = isPrime(num)
            return jsonify(prime)
        else:
            return jsonify("Please input numbers greater than 1 million")

def isPrime(num):
    if (((num-1)%6)==0) or ((num+1)%6)==0:
        return "a prime number"
    else:
        return "not a prime number"


if __name__ =="__main__":
    app.run(debug=True)
