import config

def start(bot, update):
    update.message.reply_text(config.START_TEXT)
 
def error_handler(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))