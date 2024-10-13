import os
import requests
from fastapi import FastAPI, Request
import uvicorn
import json
import pickle
import PIL
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor

app = FastAPI()


@app.post("/predict")
async def predict(request: Request):
    data = await request.json()

    if not data or "input" not in data:
        return {"error": "Неверный запрос"}

    user_input = data["input"]

    model_path = r'C:\Users\asus\Downloads\fmodel.ipynb'

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    try:
        prediction = model.predict([user_input])[0]
    except Exception as e:
        print("Ошибка при предсказании: ", e)
        return {"error": "Произошла ошибка при предсказании"}

    return {"Ответ": prediction}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
