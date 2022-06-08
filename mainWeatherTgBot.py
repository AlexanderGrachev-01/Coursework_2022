from weatherData import getNowWeather, getDayWeather, getTommorowWeather, getFiveDayWeather
from config import tg_bot_token
from aiogram import Bot, types, executor, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import Command
import markups as nav
from states import botStates

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


# *** Comands ***

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,'Hey! Write me the name of the city and I\'ll send you a weather report!'.format(message.from_user),
                           reply_markup=nav.mainMenu)

@dp.message_handler(commands=["today"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,'Write me the name of the city and I\'ll send you a weather report for today!'.format(message.from_user))
    await botStates.STATE_TODAY.set()

@dp.message_handler(commands=["tommorow"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,'Write me the name of the city and I\'ll send you a weather report for tomorrow!'.format(message.from_user))
    await botStates.STATE_TOMORROW.set()

@dp.message_handler(commands=["fivedays"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,'Write me the name of the city and I\'ll send you a weather report for five days!'.format(message.from_user))
    await botStates.STATE_FIVE_DAYS.set()

@dp.message_handler(commands=["settings"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,'It\'s a settings bar!'.format(message.from_user),  reply_markup=nav.settingsMenu)
    await botStates.STATE_SETTINGS.set()



# *** States ***

@dp.message_handler(state=botStates.STATE_NOW)
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, getNowWeather(message.text))

@dp.message_handler(state=botStates.STATE_TODAY)
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, getDayWeather(message.text))
    await botStates.STATE_NOW.set()

@dp.message_handler(state=botStates.STATE_TOMORROW)
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, getTommorowWeather(message.text))
    await botStates.STATE_NOW.set()

@dp.message_handler(state=botStates.STATE_FIVE_DAYS)
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, getFiveDayWeather(message.text))
    await botStates.STATE_NOW.set()

@dp.message_handler(state=botStates.STATE_SETTINGS)
async def get_weather(message: types.Message):
    await botStates.STATE_NOW.set()


if __name__ == '__main__':
    executor.start_polling(dp)
