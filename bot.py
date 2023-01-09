from decouple import config
from telegram import Update
from telegram.ext import Updater , CallbackContext , CommandHandler

Updater= Updater(TOKEN)
dispatcher = updater.dispatcher

def start(update: update , context: callbackcontext) :
    chat_id = update.message.chat.id
    message_id = update.message.id
    context.bot.send_message( chat_id= chat_id , text="zart" )

    
dispatcher.add_handler('start' , start)    
Updater.start_polling

token= config("TOKEN")
