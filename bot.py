import re

import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import bot_commands
import logging

TEXT_COMMANDS = {
    "Помощь": bot_commands.start,
    "Код для комнаты (.*)": bot_commands.get_room_code
}

def handle_text_command(bot, update):
    text = update.message.text
    suitable_commands = [x for x in TEXT_COMMANDS.keys() \
                         if re.search(x, text)]
    if len(suitable_commands):
        TEXT_COMMANDS[suitable_commands[0]](bot, update)
    else:
        logger.warning("WRONG INPUT: User %s sent '%s'" % \
                    (update.message.from_user.username, text))
        bot_commands.start(bot, update)

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py
    updater = Updater(config.BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", bot_commands.start))
    dp.add_handler(CommandHandler("help", bot_commands.start))
    dp.add_handler(MessageHandler(Filters.text, handle_text_command))
    updater.start_polling()
    updater.idle()
