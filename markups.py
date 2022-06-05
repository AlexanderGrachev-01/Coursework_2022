from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- Main menu ---
nowButton = KeyboardButton("Now")
tomorrowButton = KeyboardButton("Tomorrow")
fiveDaysButton = KeyboardButton("5 days")
settingsButton = KeyboardButton("Settings")
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(nowButton, tomorrowButton, fiveDaysButton, settingsButton)

# --- Settings menu ---

