import pymongo

url = ""

client = pymongo.MongoClient(url)

db = client["portfolio"]
