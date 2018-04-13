from typing import List
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters, InlineQueryHandler
from telegram.update import Update
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


eKeyboardTypeInline = 0
eKeyboardTypeReply = 1


class KeyboardConstructor(object):
    buttons: List    = []
    type             = eKeyboardTypeInline

    def __init__(self, buttons: List=None):
        self.buttons = buttons or []

    def keyboard_markup(self):
        return InlineKeyboardMarkup(self.buttons)
