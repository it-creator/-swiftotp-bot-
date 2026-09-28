import os
import asyncio
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("TOKEN")

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is Running! SwiftOTP Live"

async def start(update, context):
    await update.message.reply_text(
        "Welcome to SwiftOTP 🚀\n\nYour trusted plug for OTP services!\n\nTap /buy to get numbers."
    )

async def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is starting polling...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    print("Bot polling started!")

if __name__ == "__main__":
    # Start bot in background properly
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(run_bot())
    
    port = int(os.environ.get("PORT", 10000))
    print(f"Starting web server on port {port}")
    app_flask.run(host="0.0.0.0", port=port)
