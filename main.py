import telebot
import os
import json
from dotenv import load_dotenv

# Json user data save code
def load_data():
    try:
        with open("users.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {"users": []}

def save_data(data):
    with open("users.json", "w") as json_file:
        json.dump(data, json_file, indent=2)

def add_user(user_id,map):
    data["users"].append({"id": user_id,"map": map})

def update_user(user_id, map):
    for user in data["users"]:
        if user["id"] == user_id:
            user.update({"id": user_id,"map": map})
            break

data = load_data()
load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, botga xush kelibsiz!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()