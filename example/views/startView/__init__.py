from arch.view import *

class StartView(View):
    def __init__(self):
        super().__init__()
        self.handlers = [CommandHandler('start', self.command_start)]

    def command_start(self, bot, update: Update):
        print('start')