from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters, InlineQueryHandler
from telegram.update import Update
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from .abstract import BotAbstract
from .keyboard import KeyboardConstructor


class View(object):
    handlers: list = []
    keyboard_constructor: KeyboardConstructor

    def __init__(self, bot: BotAbstract):
        self.bot = bot
        self.handlers = []
        self.keyboard_constructor = KeyboardConstructor()
