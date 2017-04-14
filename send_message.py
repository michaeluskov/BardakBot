import config
from telegram import Bot
import db

db_users = db.users.getAllUsers()
user_ids = [x["_id"] for x in db_users]

bot = Bot(config.BOT_TOKEN)
for i in user_ids:
    bot.sendMessage(i, config.SEND_TEXT)

