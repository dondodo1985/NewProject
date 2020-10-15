import pymongo
from pymongo import MongoClient
myClient = MongoClient()
db = myClient.mydb
users = db.users
user1 = {'username':'james','password':'pass1234','favorite_number':445,'hobbies':['games','movies','sex']}
user_id = users.insert_one(user1).inserted_id