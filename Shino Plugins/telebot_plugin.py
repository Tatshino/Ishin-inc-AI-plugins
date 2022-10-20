import threading
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from json_handler import *

updater = Updater(teletoken,
                  use_context=True)

bot = telegram.Bot(token=teletoken)
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text("hiya!")
    print(update.message.chat_id)

def help(update: Update, context: CallbackContext):
  update.message.reply_text("Your Message")

def test(update: Update, context: CallbackContext):
    bot.send_message(chat_id=1501286606, text="The message system works!")
    bot.send_message(chat_id= -1001550263103, text="Hi")

def stop():
    updater.stop()
    updater.is_idle = False
    quit()
    bot.close(1)

def shutdown():
    threading.Thread(target=stop).start()

def shutdown1(update: Update, context: CallbackContext):
    threading.Thread(target=stop).start()

def chat_id(update: Update, context: CallbackContext):
    update.message.reply_text("this chats id is " + str(update.message.chat_id))

def toshi(update: Update, context: CallbackContext):
    try:
        update.message.reply_text("Toshiro should have gotten the mesage!")
        bot.send_message(chat_id=1743201932, text="use /test to say that you recieved this message")
    except:
        update.message.reply_text("I could not send Toshiro a text")

def msgMe(sentence):
    bot.send_message(chat_id=1501286606, text=sentence)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('test', test))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(CommandHandler('shutdown', shutdown1))
updater.dispatcher.add_handler(CommandHandler('chat_id', chat_id))
updater.dispatcher.add_handler(CommandHandler('toshi', toshi))
updater.dispatcher.add_handler(CommandHandler('msgMe', msgMe))

bot.send_message(chat_id=1501286606, text="I am online!")
#bot.send_message(chat_id=1665749757, text="use /test to say that you recieved this message")

# Filters out unknown messages.
#updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
