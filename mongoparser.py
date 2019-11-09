
from pymongo import MongoClient
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1f54a75f31cadcde0916ece0c91b004c"
# Your Auth Token from twilio.com/console
auth_token  = "69d01365cc53f0bc5012a777272529cd"
client = Client(account_sid, auth_token)

#this just connects to local host (27017) by default.
dbclient = MongoClient()

#get the database from the client, now it's "db"
db = dbclient.db

#get the collection from the db (users)
collection = db.users

def parse(transcript): #transcript is a string
	bigDict = {}
	for json in collection.find():  #go through all jsons in collection
		for key in json["keywords"]: #iterate through array of keywords (key is a keyword)
			if key in bigDict: #check if key is already in dict 
				bigDict[key].append(json["phone"]) #access the phone number array and append a new one
			else:
				phoneList = [json["phone"]]
				bigDict.update({key: phoneList}) #add a new keyword:phone number array pair

	transcript = set(transcript.rsplit()) #break up transcript into set of strings
	for v in transcript: #iterate through strings in transcript
		if v in bigDict: #if a string is one of the keywords
  			for pn in bigDict[v]: #interate through list of phone numbers
  				message = client.messages.create( # text all phone numbers about their keyword being mentioned.
    				to="+" + pn, 
    				from_="+12562697171",
   					body="Your keyword " + v + " was mentioned")
