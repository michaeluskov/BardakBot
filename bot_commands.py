﻿import re

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
        buttons.append([KeyboardButton("Код для комнаты " + admined_room)])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

def start(bot, update):
    user = update.message.from_user
    db_user = db.users.getOrCreateUser(user.username, user.first_name, user.last_name)
    keyboard = get_keyboard(db_user)
    update.message.reply_text(config.START_TEXT, reply_markup=keyboard)

def get_room_code(bot, update):
    username = update.message.from_user.username
    room = re.search("Код для комнаты (.*)", update.message.text)[1]
    db_user = db.users.getUser(username)
    if db_user is None or room not in db_user["admin_on"]:
        logger.warning("NOT VALID TRY TO GEN CODE: User %s tried to get code for room %s" % (username, room))
        return start(bot, update)
    code = db.codes.generateCode(room)
    text = "Код для комнаты " + room + ":"
    text = text + ".\n" * 20
    text = text + code
    keyboard = get_keyboard(db_user)
    update.message.reply_text(text, reply_markup=keyboard)

 
def error_handler(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


