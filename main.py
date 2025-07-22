
from fastapi import FastAPI, Request
from utils import generate_story_with_images

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    result = generate_story_with_images(data)
    return {"result": result}
