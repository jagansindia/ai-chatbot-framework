import os


class Config(object):
    DEBUG = False
    DB_NAME = "heroku_dj9l47s3"
    DB_HOST = "mongodb://:cadjq6j0vecegujc7jal00e7qk@ds113799.mlab.com:13799"
    DB_USERNAME = ""
    DB_PASSWORD = ""
    # Web Server details
    WEB_SERVER_PORT = 8001

    # Intent Classifier model detials
    MODELS_DIR = "model_files"
    INTENT_MODEL_NAME = "intent.model"
    DEFAULT_FALLBACK_INTENT_NAME = "fallback"
    DEFAULT_WELCOME_INTENT_NAME = "init_conversation"


class Development(Config):
    DEBUG = True


class Production(Config):
    # MongoDB Database Details
    DB_HOST = "mongodb://heroku_r98r6h3s:lceh634mfv0hv77rgs2v4ps5es@ds227469.mlab.com:27469/heroku_r98r6h3s"
    DB_USERNAME = ""
    DB_PASSWORD = ""

    # Web Server details
    WEB_SERVER_PORT = 8001
