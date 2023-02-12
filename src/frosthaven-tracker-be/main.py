from fastapi import FastAPI

from models import db
from routers import campaigns
import settings


app = FastAPI()

db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)

app.include_router(campaigns.router)
