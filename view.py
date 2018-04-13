from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters, InlineQueryHandler
from telegram.update import Update

class View:
    handlers: list = []

    def __init__(self):
        self.handlers = []