import os
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from webhook_helper import check_webhook
from bot_content_processing import process_content

def main():
    updater = Updater(os.getenv("TELEGRAM_TOKEN"), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", lambda update, context: update.message.reply_text("Бот запущен!")))
    dp.add_handler(CommandHandler("check_webhook", check_webhook))
    dp.add_handler(CommandHandler("process_content", process_content))

    updater.start_polling()
    updater.idle()