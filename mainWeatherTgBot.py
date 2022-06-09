from aiogram.dispatcher.filters import state
from weatherData import getNowWeather, getDayWeather, getTomorrowWeather, getFiveDayWeather
from config import tg_bot_token
from aiogram import Bot, types, executor, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import markups as nav
from states import botStates

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


# *** Comands ***

@dp.message_handler(commands=["start", "help"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Hey! \U0001F609\nWrite me the name of the city and I\'ll send you a weather report! \U0001F326\n\n'
                           'You can also ask me for a detailed forecast for today or '
                           'tomorrow or find out the forecast for 5 days, just use the buttons on your keyboard'.format(message.from_user),
                           reply_markup=nav.mainMenu)

@dp.message_handler(commands=["today"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Write me the name of the city and I\'ll send you a weather report for today!'.format(message.from_user))
    await botStates.STATE_TODAY.set()

@dp.message_handler(commands=["tomorrow"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Write me the name of the city and I\'ll send you a weather report for tomorrow!'.format(message.from_user))
    await botStates.STATE_TOMORROW.set()

@dp.message_handler(commands=["five_days"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Write me the name of the city and I\'ll send you a weather report for five days!'.format(message.from_user))
    await botStates.STATE_FIVE_DAYS.set()

@dp.message_handler(commands=["settings"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'It\'s a settings bar!'.format(message.from_user),
                           reply_markup=nav.settingsMenu)
    await botStates.STATE_SETTINGS.set()



# *** States ***

@dp.message_handler()
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, getNowWeather(message.text), reply_markup=nav.mainMenu)
    await dp.current_state().finish()

@dp.message_handler(state=botStates.STATE_TODAY)
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, getDayWeather(message.text), reply_markup=nav.mainMenu)
    await dp.current_state().finish()

@dp.message_handler(state=botStates.STATE_TOMORROW)
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, getTomorrowWeather(message.text), reply_markup=nav.mainMenu)
    await dp.current_state().finish()

@dp.message_handler(state=botStates.STATE_FIVE_DAYS)
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, getFiveDayWeather(message.text), reply_markup=nav.mainMenu)
    await dp.current_state().finish()

@dp.message_handler(state=botStates.STATE_SETTINGS)
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, 'Settings will be soon...', reply_markup=nav.mainMenu)
    await dp.current_state().finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
