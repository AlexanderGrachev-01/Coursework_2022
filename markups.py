from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenuButton = KeyboardButton("Main menu")

# --- Main menu ---
todayButton =KeyboardButton("/today")
tomorrowButton = KeyboardButton("/tomorrow")
fiveDaysButton = KeyboardButton("/fivedays")
settingsButton = KeyboardButton("/settings")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(todayButton,
                                                         tomorrowButton, fiveDaysButton,
                                                         settingsButton)

# --- Settings menu ---
notificationOnOfButton = KeyboardButton("On/off Notification")
notificationTimeButton = KeyboardButton("Notification time")
notificationCityButton = KeyboardButton("Change city")
settingsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(notificationOnOfButton, notificationTimeButton,
                                                             notificationCityButton, mainMenuButton)

