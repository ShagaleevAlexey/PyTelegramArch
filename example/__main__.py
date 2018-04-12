from arch.bot import *
from example.views.startView import StartView

telegram_token = '587023824:AAG9R0GlERk25stkAA2_pVdruN9USzmwaKo'

bot = Bot(telegram_token)

startView = StartView()

bot.configurate(startView)
bot.start()