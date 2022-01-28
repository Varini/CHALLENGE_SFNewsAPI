from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from db import articles
from models.articles import Article, NewArticle


app_article = APIRouter()

@app_article.get("/")
def root():
    return 'Back-end Challenge 2021 🏅 - Space Flight News'

@app_article.post("/articles/", response_description="Add new article")
async def create_article(article: Article = Body(...)):
    article = jsonable_encoder(article)    
    last_id = 0
    if articles.find_one() is not None:
        last_id = articles.find().limit(1).sort("_id", -1)[0]["id"]
    article["id"] = int(last_id) + 1
    new_article = articles.insert_one(article)
    created_article = articles.find_one({"_id": new_article.inserted_id})
    del created_article['_id']  # removes '_id' from the final response
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_article)