import json
import requests

from db import articles

start = 0

articles_collec = []

request = requests.get("https://api.spaceflightnewsapi.net/v3/articles/count")

total_articles = int(request.content.decode('utf-8'))

while True:
    r = requests.get(
        f"https://api.spaceflightnewsapi.net/v3/articles?_sort=id&_start={start}&_limit={total_articles // 10}"
    )

    documents = json.loads(r.text)

    for item in list(documents):
        articles_collec.append(item)

    if documents == []:        
            articles.insert_many(articles_collec)

    start += total_articles // 10

    if documents == []:
        break