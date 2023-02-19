"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import ephem
import logging
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(update, context):
    text = "Hi! Do you wanna know what constellation the planet is in today? Just enter it's name."
    print(text)
    update.message.reply_text(text)

def planet(update, context):
    planet_name = update.message.text
    today = datetime.date.today()
    if planet_name == 'Mercury':
      planet = ephem.Mercury(today)
      constellation = ephem.constellation(planet)
      update.message.reply_text(f'Today {planet_name} is in the {constellation}')  
    elif planet_name == 'Venus':
      planet = ephem.Venus(today)
      constellation = ephem.constellation(planet)
      update.message.reply_text(f'Today {planet_name} is in the {constellation}')  
    elif planet_name == 'Mars':
      planet = ephem.Mars(today)
      constellation = ephem.constellation(planet)
      update.message.reply_text(f'Today {planet_name} is in the {constellation}')
    elif planet_name == 'Jupiter':
      planet = ephem.Jupiter(today)
      constellation = ephem.constellation(planet)
      update.message.reply_text(f'Today {planet_name} is in the {constellation}')  
    elif planet_name == 'Saturn':
      planet = ephem.Saturn(today)
      constellation = ephem.constellation(planet)
      update.message.reply_text(f'Today {planet_name} is in the {constellation}') 
    elif planet_name == 'Uranus':
      planet = ephem.Uranus(today)
      constellation = ephem.constellation(planet)
      update.message.reply_text(f'Today {planet_name} is in the {constellation}')  
    elif planet_name == 'Neptun':
      planet = ephem.Neptun(today)
      constellation = ephem.constellation(planet)
      update.message.reply_text(f'Today {planet_name} is in the {constellation}')
    
    else:
      update.message.reply_text("I don't know this planet.")



def main():
    mybot = Updater("5805847240:AAFrZY8X5otrQH3APnH_roJArWeiprC6QBY", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
