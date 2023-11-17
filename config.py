import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 21627756))

    API_HASH = os.environ.get("API_HASH", "b20b095ccaab92fe64d8e765549a9219")

    