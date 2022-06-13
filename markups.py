from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenuButton = KeyboardButton("Menu")
backButton = KeyboardButton("Back")

backMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
backMenu.add(backButton)

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
notificationTimeButton = KeyboardButton("Notification_time")
notificationCityButton = KeyboardButton("Notification_city")

settingsMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
settingsMenu.add(notificationOnOfButton, notificationTimeButton, notificationCityButton, mainMenuButton)

# --- Notification on / off  ---
notificationOnButton = KeyboardButton("Turn on")
notificationOffButton = KeyboardButton("Turn off")

notificationOnOffMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
notificationOnOffMenu.add(notificationOnButton, notificationOffButton).add(backButton)






