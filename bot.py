import config
import telebot
from pycbrf import ExchangeRates
from datetime import date

today = date.today()
rates = ExchangeRates(today)
bot = telebot.TeleBot(config.TOKEN)
rates = ExchangeRates('2022-06-12')
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, "данный бот является калькулятором валют, на данный момент он работает только с Российскими рублями)")
	bot.send_message(message.chat.id, "для показа команд /help")

@bot.message_handler(commands=["help"])
def start(message):
	bot.send_message(message.chat.id, "/usd - курс доллара США")
	bot.send_message(message.chat.id, "/eur - курс ЕВРО")
	bot.send_message(message.chat.id, "/byn - курс Беллоруского рубля")
	bot.send_message(message.chat.id, "/pln - курс Польского злотого")
	bot.send_message(message.chat.id, "/gbp - курс Британского фунта")
	bot.send_message(message.chat.id, "/cny - курс Китайского юаня")
	bot.send_message(message.chat.id, "/chf - курс Швейцарского франка")
	bot.send_message(message.chat.id, "/czk - курс Чешской кроны")	

@bot.message_handler(commands=["usd"])
def usd(message):
	text = "1 Доллар США ="+str(rates['USD'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["gbp"])
def usd(message):
	text = "1 Британский фунт ="+str(rates['GBP'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["cny"])
def usd(message):
	text = "1 Китайский юань ="+str(rates['CNY'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["eur"])
def usd(message):
	text = "1 Евро ="+str(rates['EUR'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["chf"])
def usd(message):
	text = "1 Швейцарский франк ="+str(rates['CHF'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["czk"])
def usd(message):
	text = "1 Чешская крона ="+str(rates['CZK'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["pln"])
def usd(message):
	text = "1 Польский злотый ="+str(rates['PLN'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["byn"])
def usd(message):
	text = "1 Белорусский рубль ="+str(rates['BYN'].rate)+"руб."
	bot.send_message(message.chat.id, text)

if __name__ == '__main__':
	bot.infinity_polling()