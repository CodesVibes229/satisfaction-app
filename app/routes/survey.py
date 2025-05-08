from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/surveys", tags=["Surveys"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.SurveyOut)
def create_survey(survey: schemas.SurveyCreate, db: Session = Depends(get_db)):
    db_survey = models.Survey(**survey.dict())
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey
