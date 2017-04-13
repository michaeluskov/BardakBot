import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import db

def on_message(bot, update):
    user = update.message.from_user
    
    logger.info("User %s sent '%s'" % (user.username or user.id, update.message.text))
    db_user = db.users.getOrCreateUser(user.id, user.username, user.first_name, user.last_name)
    update.message.reply_text(config.IDLE_TEXT)

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    logger = logging.getLogger(__name__)
    logFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler = logging.FileHandler("./log.txt")
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)
    
    # https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py
    updater = Updater(config.BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", on_message))
    dp.add_handler(MessageHandler(Filters.text, on_message))
    updater.start_polling()
    logger.info("Idle bot started")
    updater.idle()
