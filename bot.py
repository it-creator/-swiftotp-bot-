import os, threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return "SwiftOTP Bot Running!"
def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Welcome to SwiftOTP 🚀\nYour trusted plug for US/UK OTPs.\n\n🔥 USA OTP - ₦2,000 Instant Delivery"
    keyboard = [[InlineKeyboardButton("🛒 Buy Now", url="https://swiftotp.sell.app/product/usa-otp-instant-delivery")]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def buy(u,c): await u.message.reply_text("Buy: https://swiftotp.sell.app/product/usa-otp-instant-delivery")
async def myorders(u,c): await u.message.reply_text("Check your email from SellApp")
async def support(u,c): await u.message.reply_text("Support: @herbertofili")
async def help_cmd(u,c): await u.message.reply_text("/start /buy /myorders /support")

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("myorders", myorders))
    app.add_handler(CommandHandler("support", support))
    app.add_handler(CommandHandler("help", help_cmd))
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    run_bot()
- Click *Commit changes*

   - Again *Add file → Create new file*
   - File name: `requirements.txt`
   - Content:
python-telegram-bot==20.7
flask .commit
