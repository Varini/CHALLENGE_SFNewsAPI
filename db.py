from bson import ObjectId
from pymongo import MongoClient
from dotenv import dotenv_values, load_dotenv

import json
import requests

config = dotenv_values("D:\Git\CHALLENGE_SFNewsAPI_DEV\.env")

conn = MongoClient(config['CONNECT_STR'])

db = conn.sfnewsDB

articles = db.articles