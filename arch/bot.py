from arch.view import *

class Navigator:
    def __init__(self):
        pass

class Bot:
    updater: Updater
    token = ''  #type: str
    navigator = Navigator()

    def __init__(self, token: str):
        self.token = token
        self.updater = Updater(self.token)

    def configurate(self, view: View):
        dp = self.updater.dispatcher

        for handler in view.handlers:
            dp.add_handler(handler)

    def start(self):
        self.updater.start_polling()
        self.updater.idle()