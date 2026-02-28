from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import ChatRequest, Expense
from services.core import categorize_expense

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    return {"message": req.message}

@router.post("/expenses")
def create_expense(expense: Expense):
    categorized_expense = categorize_expense(expense)
    return categorized_expense