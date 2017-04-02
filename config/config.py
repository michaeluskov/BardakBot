import os.path

BOT_TOKEN = "TELEGRAMBOTTOKEN"
MONGODB_URL = "mongodb://localhost:27017/bardakbot"

START_TEXT = """Привет!
Это бот на Бардак.
Текст мы потом перепишем.
"""

# -------------------------------------------------------------------------------------
if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/config_local.py"):
    print("You can set your own local settings in config/config_local.py")
else:
    from .config_local import *
