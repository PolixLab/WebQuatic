from pymongo import MongoClient

client = MongoClient('insert your mongodb connection')

db = client.centauro

#collection = db.test.find()
#print collection
#for element in collection:
 # print element

def newuser(data):
 db.test.insert(data)
