from telegram.ext import Updater, CommandHandler
import requests
import re
import random

def get_dog_url():
    contents = requests.get('https://random.dog/woof.json').json() 
    print("Contents je ", contents)   
    url = contents['url']
    print("URL je ", url)
    return url
    
def get_cat_url():
    contents = requests.get('http://aws.random.cat/meow').json() 
    url = contents['file']
    return url

def get_name(update):
    print("Mowiym z ", update.message.chat.first_name)
    return update.message.chat.first_name
    
def dog(bot, update):
    url = get_dog_url()
    
    
    name = get_name(update)
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    bot.send_message(chat_id=chat_id, text="Woof " + name)
    
def cat(bot, update):
    url = get_cat_url()
    name = get_name(update)
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    bot.send_message(chat_id=chat_id, text="Meow " + name)

def zara(bot, update):
    zarzine_fotki = ["https://www.instagram.com/p/Bdf4AKIgsmg/", "https://www.instagram.com/p/Bj5UwStAfee/", "https://www.instagram.com/p/Bdf51JLgJLj/", "https://www.instagram.com/p/Bdf43zDALaC/"]
    url = random.choice(zarzine_fotki)
    name = get_name(update)
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    bot.send_message(chat_id=chat_id, text="Haf " + name)

def korona(bot, update):
    try:
        print("W koronie")
        contents = requests.get('https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/nakaza.min.json').json()
        chat_id = update.message.chat_id
        celkem=str(contents[-1]['pocetCelkem'])
        den=str(contents[-1]['pocetDen'])
        bot.send_message(chat_id=chat_id, text='Day: ' + den + ' total: ' + celkem)
    except Error as e:
        print("An exception occurredddd", e)


def main():
    updater = Updater('971782121:AAG6pwh2j7gWw2_zahEOfGfxcn8wNuTNgGk')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dejpiesa',dog))
    dp.add_handler(CommandHandler('dejkota',cat))
    dp.add_handler(CommandHandler('dejzare',zara))
    dp.add_handler(CommandHandler('korona',korona))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()    
