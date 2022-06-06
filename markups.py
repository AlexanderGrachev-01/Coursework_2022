from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenuButton = KeyboardButton("Main menu")

# --- Main menu ---
todayButton =KeyboardButton("Today")
tomorrowButton = KeyboardButton("Tomorrow")
fiveDaysButton = KeyboardButton("5 days")
settingsButton = KeyboardButton("Settings")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(todayButton,
                                                         tomorrowButton, fiveDaysButton,
                                                         settingsButton)

# --- Settings menu ---
notificationOnOfButton = KeyboardButton("On/off Notification")
notificationTimeButton = KeyboardButton("Notification time")
notificationCityButton = KeyboardButton("Change city")
settingsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(notificationOnOfButton, notificationTimeButton,
                                                             notificationCityButton, mainMenuButton)

