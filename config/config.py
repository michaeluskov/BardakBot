import os.path

BOT_TOKEN = "TELEGRAMBOTTOKEN"
MONGODB_URL = "mongodb://localhost:27017/"
MONGODB_DATABASE = "bardakbot"

START_TEXT = """Привет!
Это бот на Бардак.
Текст мы потом перепишем.
"""

ROOMS_TEXT = """Тут будет список комнат.
"""

IDLE_TEXT = """Привет! Я бот, который поможет тебе ориентироваться на Бардаке. Я начну работать в полную силу сразу после начала Бардака.
А еще я щедрый и раздаю призы. Как их получить? Просто успей пройти все комнаты до конца мероприятия :) Получай в каждой комнате код и шли его мне.
Ну все, до субботы! Не забывай меня.
"""

SEND_TEXT = """Я отправлю этот текст.
"""

# -------------------------------------------------------------------------------------
if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/config_local.py"):
    print("You can set your own local settings in config/config_local.py")
else:
    from .config_local import *
