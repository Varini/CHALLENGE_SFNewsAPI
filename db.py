import json
import ctypes
import requests

from bson import ObjectId
from pymongo import MongoClient
from dotenv import dotenv_values, load_dotenv

config = dotenv_values(".env")

conn = MongoClient(config['CONNECT_STR'])

db = conn.sfnewsDB

articles = db.articles

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def db_sync():

    try:

        print("Syncing Articles...")

        sync = 1

        start = 0

        articles_collec = []

        last_id = 0
        if articles.find_one() is not None:
            last_id = (articles.find().limit(1).sort("_id", -1))[0]["id"]

        request = requests.get(
            "https://api.spaceflightnewsapi.net/v3/articles/count")

        total_articles = int(request.content.decode('utf-8'))

        while sync:
            r = requests.get(
                f"https://api.spaceflightnewsapi.net/v3/articles?_start={start}&_limit={total_articles // 100}"
            )
            documents = json.loads(r.text)

            for doc in list(documents):
                article = articles.find_one({"title": doc.get("title"), "url": doc.get("url"), "imageUrl": doc.get("imageUrl"), 
                                            "newsSite": doc.get("newsSite"), "summary": doc.get("summary"), 
                                            "publishedAt": doc.get("publishedAt")})

                if article == None:
                    last_id += 1
                    doc["id"] = last_id
                    articles_collec.append(doc)
                    print(f'Inserting new article "{doc.get("title")}"...')
                else:
                    articles_tosync = len(articles_collec)

                    if articles_tosync != 0:
                        print(f"Total of articles to sync: {articles_tosync}")

                        articles.insert_many(articles_collec)

                        print("Synchronization completed!")
                    else:
                        print("No sync needed.")

                    sync = 0

                    break

            start += total_articles // 100

    except Exception as error:
        Mbox('Synchronization failed!', 'Some failure occurred while syncing articles.', 0)        