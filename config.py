import os


class Config(object):
    DEBUG = False
    DB_NAME = "heroku_dj9l47s3"
    DB_HOST = "mongodb://ds113799.mlab.com:13799"
    DB_USERNAME = "heroku_dj9l47s3"
    DB_PASSWORD = "heroku_dj9l47s3"
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
    DB_HOST = "mongodb://mongodb:27017/"
    DB_USERNAME = ""
    DB_PASSWORD = ""

    # Web Server details
    WEB_SERVER_PORT = 8001
