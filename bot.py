from .abstract import BotAbstract
from .view import Updater
from typing import List

class Navigator(object):

    def __init__(self):
        pass


class Bot(BotAbstract):

    updater: Updater
    token: str
    views: List
    navigator: Navigator

    def __init__(self, token: str):
        self.token = token
        self.updater = Updater(self.token)
        self.views = []

    def configurate(self, views: List):
        dp = self.updater.dispatcher

        handlers = [view.handlers for view in views]
        # [dp.add_handler(handler) for handler in [view.handlers for view in views] if handler is not None]

    def start(self):
        self.updater.start_polling()
        self.updater.idle()