from pymongo import MongoClient

client = MongoClient("<connection string>")
db = client.sfnewsDB
articles = db["articles"]

articles = db.articles