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
		# url = "https://onemocneni-aktualne.mzcr.cz/covid-19"
		url = "http://bit.ly/3231YVs"
		contents = requests.get('https://onemocneni-aktualne.mzcr.cz/covid-19').json()
		print(contents) 
		name = get_name(update)
		chat_id = update.message.chat_id
		bot.send_photo(chat_id=chat_id, photo=url)
		bot.send_message(chat_id=chat_id, text="Haf " + name)
	except Error as e:
		print("An exception occurred", e)


def main():
    updater = Updater('971782121:AAG6pwh2j7gWw2_zahEOfGfxcn8wNuTNgGk')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dejpiesa',dog))
    dp.add_handler(CommandHandler('dejkota',cat))
    dp.add_handler(CommandHandler('dejzare',zara))
    # dp.add_handler(CommandHandler('korona',korona))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()    
