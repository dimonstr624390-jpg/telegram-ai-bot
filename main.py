import telebot
from config import token
from logic import get_class
import tf_keras as keras
from tf_keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я твой бот")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    image = "image.jpg"  # Путь к изображению
    model_path = "model/keras_model.h5"
    labels_path = "model/labels.txt"
    result = get_class(image, model_path, labels_path)
    bot.reply_to(message, result)
    
bot.infinity_polling()