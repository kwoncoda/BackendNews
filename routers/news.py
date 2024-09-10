from fastapi import APIRouter
from database import mysql_create_session

router = APIRouter(
  prefix="/news",
  tags=["news"]
)

@router.get("/")
def tmp_news():
  return "HELLO WORLD"


