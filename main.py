from fastapi import FastAPI
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()


@app.get("/")
async def action_magna_class():
    return {"Hello": os.getenv("MY_VAR")}
