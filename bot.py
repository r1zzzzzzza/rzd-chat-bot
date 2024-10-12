# bot

import telebot
from telebot import types

token='7384184406:AAF-kbng8DTneTN75WPA5_ZgG9yUgI8ZFzE'

bot=telebot.TeleBot('7384184406:AAF-kbng8DTneTN75WPA5_ZgG9yUgI8ZFzE')
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, "Привет! Я - ваш электронный помощник по документации. Чем я могу вам помочь?")
bot.infinity_polling()

# api model???

import requests
from fastapi import FastAPI, Request
import uvicorn
import json
import pickle
import torch
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor

app = FastAPI()

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()

bot_token = '7384184406:AAF-kbng8DTneTN75WPA5_ZgG9yUgI8ZFzE'
api_url = 'http://localhost:8000/predict'

# Получаем текстовое сообщение от пользователя
user_input = input()
def question(user_input):

    #Логика предсказания модели
    model_path = 'rhymes-ai/Aria'
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict([user_input])[0]

    return {"Ответ:": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

payload = {"data": user_input}
headers = {'Content-Type': 'application/json'}
# запуск модели
response = requests.post(api_url, json=payload, headers=headers)
print(response.text)