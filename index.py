import uvicorn
from fastapi import FastAPI

from routes.articles import app_article

app = FastAPI()

app.include_router(app_article)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    