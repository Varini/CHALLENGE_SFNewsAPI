from fastapi import APIRouter

app_article = APIRouter()

@app_article.get("/")
def root():
    return 'Back-end Challenge 2021 🏅 - Space Flight News'