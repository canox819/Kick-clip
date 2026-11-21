
import os
import re
import telebot
from telebot import types

TOKEN = os.getenv"9255966595:AAGL1Z4g9M3eWyR9F6gY1d7RK562NCfjdMM"

if not TOKEN:
    raise RuntimeError("BOT_TOKEN bulunamadı!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    keyboard.add("🎬 Yayın analiz et")
    keyboard.add("📂 Kliplerim", "⚙️ Ayarlar")

    bot.send_message(
        message.chat.id,
        "KICK CLIP'e hoş geldin!\n\n"
        "Kick yayın veya VOD bağlantısını gönder.",
        reply_markup=keyboard
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "/start - Botu başlat\n"
        "/help - Yardım"
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text or ""

    if re.search(r"https?://(?:www\.)?kick\.com/", text, re.I):
        bot.reply_to(
            message,
            "Bağlantı alındı!\n"
            "Video analiz sistemi henüz hazırlanıyor."
        )
    else:
        bot.reply_to(
            message,
            "Lütfen geçerli bir Kick yayın bağlantısı gönder."
        )

if __name__ == "__main__":
    print("KICK CLIP çalışıyor!")
    bot.infinity_polling()
