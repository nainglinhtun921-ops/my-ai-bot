import os, asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("မင်္ဂလာပါ။ ဖုန်း CPU လုံးဝမသုံးဘဲ Cloud ပေါ်က Run ထားတဲ့ AI Bot ဖြစ်ပါတယ်။")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        response = model.generate_content(update.message.text)
        await update.message.reply_text(response.text)
    except:
        await update.message.reply_text("ခဏလေးပါဗျာ၊ AI ချက်လုပ်မှု စစ်ဆေးနေလို့ပါ။")

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()

