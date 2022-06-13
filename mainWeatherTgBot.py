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
                           'tomorrow or find out the forecast for 5 days, just use the buttons on your keyboard',
                           reply_markup=nav.mainMenu)

@dp.message_handler(commands=["today"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Write me the name of the city and I\'ll send you a weather report for today!')
    await botStates.STATE_TODAY.set()

@dp.message_handler(commands=["tomorrow"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Write me the name of the city and I\'ll send you a weather report for tomorrow!')
    await botStates.STATE_TOMORROW.set()

@dp.message_handler(commands=["five_days"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Write me the name of the city and I\'ll send you a weather report for five days!')
    await botStates.STATE_FIVE_DAYS.set()

@dp.message_handler(commands=["settings"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'It\'s a settings bar!',
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
async def settings(message: types.Message):
    if message.text == 'On/off Notification':
        await bot.send_message(message.from_user.id,
                               'Do you want to receive notifications? \U0001F514',
                               reply_markup=nav.notificationOnOffMenu)
        await botStates.STATE_ON_OFF.set()
    else:
        if message.text == 'Notification_time':
            await bot.send_message(message.from_user.id,
                                   'When do you want to receive notifications? \U000023F0',
                                   reply_markup=nav.backMenu)
            await botStates.STATE_TIME.set()
        else:
            if message.text == 'Notification_city':
                await bot.send_message(message.from_user.id,
                                       'Which city do you want to receive notifications from? \U0001F3D9',
                                       reply_markup=nav.backMenu)
                await botStates.STATE_CITY.set()
            else:
                if message.text == 'Menu':
                    await bot.send_message(message.from_user.id,
                                           'Write me the name of the city and I\'ll send you a weather report! \U0001F326',
                                           reply_markup=nav.mainMenu)
                    await dp.current_state().finish()


@dp.message_handler(state=botStates.STATE_ON_OFF)
async def on_off_notification(message: types.Message):
    if message.text == 'Turn on':
        await bot.send_message(message.from_user.id,
                               'Notifications turn on \U0001F514',
                               reply_markup=nav.notificationOnOffMenu)
    else:
        if message.text == 'Turn off':
            await bot.send_message(message.from_user.id,
                                   'Notification turn off \U0001F515',
                                   reply_markup=nav.notificationOnOffMenu)
        else:
            if message.text == 'Back':
                await bot.send_message(message.from_user.id,
                                       'It\'s a settings bar!'.format(message.from_user),
                                       reply_markup=nav.settingsMenu)
                await botStates.STATE_SETTINGS.set()


@dp.message_handler(state=botStates.STATE_TIME)
async def notification_time(message: types.Message):
    if message.text == 'Back':
        await bot.send_message(message.from_user.id,
                               'It\'s a settings bar!'.format(message.from_user),
                               reply_markup=nav.settingsMenu)
        await botStates.STATE_SETTINGS.set()
    else:
        await bot.send_message(message.from_user.id,
                               f'Notification time changed to {message.text}',
                               reply_markup=nav.settingsMenu)
        await botStates.STATE_SETTINGS.set()


@dp.message_handler(state=botStates.STATE_CITY)
async def notification_city(message: types.Message):
    if message.text == 'Back':
        await bot.send_message(message.from_user.id,
                               'It\'s a settings bar!'.format(message.from_user),
                               reply_markup=nav.settingsMenu)
        await botStates.STATE_SETTINGS.set()
    else:
        await bot.send_message(message.from_user.id,
                               f'Notification city changed to "{message.text}"',
                               reply_markup=nav.settingsMenu)
        await botStates.STATE_SETTINGS.set()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
