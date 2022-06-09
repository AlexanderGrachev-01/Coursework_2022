from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenuButton = KeyboardButton("Main menu")

# --- Main menu ---
helpButton = KeyboardButton("/help")
todayButton = KeyboardButton("/today")
tomorrowButton = KeyboardButton("/tomorrow")
fiveDaysButton = KeyboardButton("/five_days")
settingsButton = KeyboardButton("/settings")

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
mainMenu.add(todayButton, tomorrowButton, fiveDaysButton,).add(helpButton, settingsButton)

# --- Settings menu ---
notificationOnOfButton = KeyboardButton("On/off Notification")
notificationTimeButton = KeyboardButton("Notification time")
notificationCityButton = KeyboardButton("Change city")

settingsMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
settingsMenu.add(notificationOnOfButton, notificationTimeButton, notificationCityButton, mainMenuButton)

