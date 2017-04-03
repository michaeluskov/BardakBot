import config
import db
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram import KeyboardButton

def get_keyboard(username):
    buttons = [
        [KeyboardButton("/start")],
        [KeyboardButton("/help")]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

def start(bot, update):
    keyboard = get_keyboard(update.message.from_user.username)
    user = update.message.from_user
    db.users.getOrCreateUser(user.username, user.first_name, user.last_name)
    update.message.reply_text(config.START_TEXT, reply_markup=keyboard)
 
def error_handler(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
