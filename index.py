import uvicorn
import warnings
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler

from db import db_sync

from routes.articles import app_article

warnings.filterwarnings('ignore')

app = FastAPI()

app.include_router(app_article)

app.on_event("startup")


def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(id="db_sync", func=db_sync, trigger="cron",
                      hour="9", minute="00", second="00")
    scheduler.start()


if __name__ == "__main__":
    init_scheduler()
    uvicorn.run(app="index:app", host="0.0.0.0",
                port=8000, reload=False, debug=False)
