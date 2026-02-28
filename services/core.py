import httpx
import os
from dotenv import load_dotenv
from models import Expense

load_dotenv()
GPT_API_KEY = os.getenv("GPT_API_KEY")

async def categorize_expense(expense: Expense):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/completions",
            headers={"Authorization": f"Bearer {GPT_API_KEY}"},
            json={
                "model": "text-davinci-003",
                "prompt": f"Categorize the expense: {expense.description}",
                "max_tokens": 1024,
                "temperature": 0.7
            }
        )
        category = response.json()["choices"][0]["text"]
        return {"amount": expense.amount, "description": expense.description, "category": category}