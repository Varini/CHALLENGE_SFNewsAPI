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


@app_article.get("/articles/", response_description="List all articles", response_model=list[Article])
async def list_articles(page_num: int = 0, page_size: int = 10):

    # 'n' in DB[articlestion].find.skip(n) must be >= 0
    if page_num < 0:
        page_num = 0

    # Skip and limit
    cursor = articles.find().skip(
        page_num).limit(page_size).sort("_id", -1)

    # Return documents
    return [x for x in cursor]


@app_article.get(
    "/articles/{id}", response_description="Get a single article", response_model=Article
)
async def show_article(id: int):
    if (article := articles.find_one({"id": id})) is not None:
        return article

    raise HTTPException(status_code=404, detail=f"Article ID: {id} not found")


@app_article.put("/articles/{id}", response_description="Update an article", response_model=Article)
async def update_article(id: int, article: NewArticle = Body(...)):
    article = {k: v for k, v in article.dict().items() if v is not None}

    if len(article) >= 1:
        update_result = articles.update_one(
            {"id": id}, {"$set": article})

        if update_result.modified_count == 1:
            if (
                updated_article := articles.find_one({"id": id})
            ) is not None:
                return updated_article

    if (existing_article := articles.find_one({"id": id})) is not None:
        return existing_article

    raise HTTPException(status_code=404, detail=f"Article ID: {id} not found")


@app_article.delete("/articles/{id}", response_description="Delete an article")
async def delete_article(id: int):
    delete_result = articles.delete_one({"id": id})

    if delete_result.deleted_count == 1:
        return f"article ID: {id} was deleted."

    raise HTTPException(status_code=404, detail=f"Article ID: {id} not found")
