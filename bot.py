import os, asyncio, threading
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

TOKEN = os.getenv("TOKEN")
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "SwiftOTP Live"

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("🛒 Buy OTP", callback_data="buy")],
        [InlineKeyboardButton("📞 Support", url="https://t.me/herbertofili")]
    ]
    await update.message.reply_text(
        "Welcome to SwiftOTP 🚀\n\n"
        "Your trusted plug for instant OTP services!\n\n"
        "🇺🇸 USA Numbers • ⚡️ Instant Delivery\n"
        "Tap Buy below 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buy(update, context):
    keyboard = [[InlineKeyboardButton("✅ Buy Now on Sell.app", url="https://swiftotp.sell.app/product/usa-otp-instant-delivery")]]
    text = (
        "🔥 USA OTP - INSTANT DELIVERY 🔥\n\n"
        "✅ Services: WhatsApp | Gmail | Telegram | Tinder | Others\n"
        "💰 Price: ₦4,000\n"
        "📦 Stock: Unlimited\n"
        "⚡️ Delivery: <1 minute\n\n"
        "Click below to purchase 👇"
    )
    if update.callback_query:
        await update.callback_query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
        await update.callback_query.answer()
    else:
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update, context):
    query = update.callback_query
    if query.data == "buy":
        await buy(update, context)

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot polling started!")
    app.run_polling(stop_signals=None, close_loop=False)

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    app_flask.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
