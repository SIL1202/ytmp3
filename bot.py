from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import subprocess
import uuid
import os

# 這裡貼上你的 BotFather Token
BOT_TOKEN = '7727514995:AAFUfBHkZpYzphEAClEBbwLOFAZ7oDYBxrU'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("嗨！貼上 YouTube 連結，我幫你轉成 MP3 🎵")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    filename = str(uuid.uuid4()) + ".mp3"
    try:
        command = f"yt-dlp -x --audio-format mp3 -o '{filename}' {url}"
        subprocess.run(command, shell=True, check=True)
        await update.message.reply_audio(audio=open(filename, "rb"))
    except Exception as e:
        await update.message.reply_text(f"發生錯誤了！{e}")
    finally:
        if os.path.exists(filename):
            os.remove(filename)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot 正在啟動...")
app.run_polling()
