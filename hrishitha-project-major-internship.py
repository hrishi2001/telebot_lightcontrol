! pip install python-telegram-bot
! pip install adafruit-io
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import Update
import requests
from Adafruit_IO import Client,Data
import os
def turnoff(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Led turned off")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://tse3.mm.bing.net/th?id=OIP.VnOW7P6iZ7sc_xq90KgZcgHaHa&pid=Api&P=0&w=300&h=300')
  send_value(0)
def turnon(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Led turned on")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://tse3.mm.bing.net/th?id=OIP.TCWC_VI2VD81i9jr-ys7PQHaE7&pid=Api&P=0&w=250&h=167')
  send_value(1)
def send_value(value):
  feed = aio.feeds('light')
  aio.send_data(feed.key,value)

def input_message(update, context):
  text=update.message.text
  if text == 'turn on':
    send_value(1)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Led turned on")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://tse3.mm.bing.net/th?id=OIP.TCWC_VI2VD81i9jr-ys7PQHaE7&pid=Api&P=0&w=250&h=167')
  elif text == 'turn off':
    send_value(0)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Led turned off")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://tse3.mm.bing.net/th?id=OIP.VnOW7P6iZ7sc_xq90KgZcgHaHa&pid=Api&P=0&w=300&h=300')

def start(update,context):
  start_message='''
/turnoff or 'turn off':To turn of the led ,sends value=0 in feed
/turnon or 'turn on'  :To turn on the led ,sends value=1 in feed
'''
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)
  ADAFRUIT_IO_USERNAME = os.getenv('hrishi_2001')  #username declared
ADAFRUIT_IO_KEY = os.getenv('aio_SAfP37Kcd97pLeG7FA8gFyYiISFp')  #io key declared
TOKEN = os.getenv('1104507848:AAGFPfk5kIqZz2JXHYyIebnGYV581MZlXsE')  #token declared
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
updater=Updater(TOKEN,use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('turnoff',turnoff))
dispatcher.add_handler(CommandHandler('turnon',turnon))
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
updater.start_polling()
updater.idle()
