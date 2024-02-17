from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def action_magna_class():
    return {"Hello": "Magna Class"}
