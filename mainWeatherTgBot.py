from weatherData import getNowDayWeather
from config import tg_bot_token
from aiogram import Bot, types, executor, Dispatcher
import markups as nav

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,'Hey! Write me the name of the city and I\'ll send you a weather report!'.format(message.from_user),
                           reply_markup=nav.mainMenu)

@dp.message_handler()
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, getNowDayWeather(message.text))



if __name__ == '__main__':
    executor.start_polling(dp)
