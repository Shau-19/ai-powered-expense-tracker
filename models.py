from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class Expense(BaseModel):
    amount: float
    description: str
    category: str = ""