
from pymongo import MongoClient

#this just connects to local host (27017) by default.
client = MongoClient()

#get the database from the client, now it's "testdb"
db = client.db

#get the collection from the db, it's the same name
collection = db.users

bigDict = {}

def buildDict():
	for json in collection.find():  #go through all jsons in collection
		print(json)
		for key in json["keywords"]: #iterate through array of keywords (key is a keyword)
			if key in bigDict: #check if key is already in dict 
				bigDict[key].append(json["phone"]) #access the phone number array and append a new one
			else:
				phoneList = [json["phone"]]
				bigDict.update({key: phoneList}) #add a new keyword:phone number array pair
	print(bigDict)

buildDict()





