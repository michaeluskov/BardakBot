import re

import config
import db
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram import KeyboardButton
import logging

logger = logging.getLogger(__name__)

def get_keyboard(db_user):
    buttons = [
        [KeyboardButton("Помощь")]
    ]
    for admined_room in db_user["admin_on"]:
        buttons[0].append(KeyboardButton("Код для комнаты " + admined_room))
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

def start(bot, update):
    user = update.message.from_user
    db_user = db.users.getOrCreateUser(user.username, user.first_name, user.last_name)
    keyboard = get_keyboard(db_user)
    update.message.reply_text(config.START_TEXT, reply_markup=keyboard)

def get_room_code(bot, update):
    username = update.message.from_user.username
    room = "TEST_ROOM"
    db_user = db.users.getUser(username)
    if db_user is None or room not in db_user["admin_on"]:
        logger.warning("NOT LOGGED IN TRY TO GEN CODE: User %s tried to get code for room %s" % (username, room))
        return start(bot, update)
    keyboard = get_keyboard(db_user)
    update.message.reply_text("Код для комнаты", reply_markup=keyboard)

 
def error_handler(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


