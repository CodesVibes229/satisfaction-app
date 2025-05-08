from fastapi import FastAPI
from routes import survey  # <--- plus de point

app = FastAPI(title="Satisfaction Survey API")

app.include_router(survey.router)
