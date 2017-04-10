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
    if db_user is not None:
        for admined_room in db_user["admin_on"]:
            buttons.append([KeyboardButton("Код для комнаты " + admined_room)])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

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
    text += ".\n" * 20
    text += code
    keyboard = get_keyboard(db_user)
    update.message.reply_text(text, reply_markup=keyboard)

def handle_code_input(bot, update):
    username = update.message.from_user.username
    db_user = db.users.getUser(username)
    if db_user is None:
        return start(bot, update)
    code = update.message.text
    code_from_db = db.codes.checkCode(code)
    if code_from_db is None:
        return update.message.reply_text("Нет такого кода! Переспроси организатора", \
                                         reply_markup=get_keyboard(db_user))
    db.codes.activateCode(code)
    if code_from_db["room_name"] not in db_user["passed"]:
        db_user["passed"].append(code_from_db["room_name"])
    db.users.updateUser(db_user)
    rooms_string = ", ".join(db_user["passed"])
    update.message.reply_text("Код для комнаты %s засчитан! Ты прошел комнаты: %s" % \
                              (code_from_db["room_name"], rooms_string), \
                              reply_markup=get_keyboard(db_user))


 
def error_handler(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


