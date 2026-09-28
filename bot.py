import os
import asyncio
import threading
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("TOKEN")

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is Running!"

async def start(update, context):
    await update.message.reply_text(
        "Welcome to SwiftOTP 🚀\n\nYour trusted plug for OTP services!\n\nTap /buy to get numbers."
    )

def run_bot():
    # Fix for Render threading error
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)
