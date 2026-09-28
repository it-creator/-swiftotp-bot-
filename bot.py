import os
import asyncio
import threading
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("TOKEN")

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "SwiftOTP Live - Bot Running"

async def start(update, context):
    await update.message.reply_text(
        "Welcome to SwiftOTP 🚀\n\nYour trusted plug for OTP services!\n\nTap /buy to get numbers."
    )

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        print("Starting bot polling...")
        app.run_polling(stop_signals=None, close_loop=False)
    except Exception as e:
        print(f"BOT ERROR: {e}")

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)
