import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import bot_commands
import logging

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py
    updater = Updater(config.BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", bot_commands.start))
    dp.add_handler(CommandHandler("help", bot_commands.start))
    dp.add_handler(MessageHandler(Filters.text, bot_commands.handle_text_command))
    updater.start_polling()
    updater.idle()
