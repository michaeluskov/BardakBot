import config
from telegram import Bot
import db
import time
import pprint

db_users = db.users.getAllUsers()
user_ids = [x["_id"] for x in db_users]

bot = Bot(config.BOT_TOKEN)
for num, i in enumerate(user_ids):
    print("Sending message to %s" % i)
    if num % 10 == 0:
        time.sleep(7)
    try:
        bot.sendMessage(i, config.SEND_TEXT)
    except Exception as e:
        pprint.pprint(e)
        

