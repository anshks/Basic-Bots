import logging
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

updater = Updater(token='748769185:AAG6Yr5PO9a6_79KoIniqbQQ9DE1SoWYIU4')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def startKey(bot, update):
    keyboard = [[InlineKeyboardButton("12 hr format", callback_data='1'),
                 InlineKeyboardButton("24 hr format", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    if format(query.data) == "2":
        date_time = str(datetime.now()).split()
        date,time = date_time
        bot.edit_message_text(text=str(time)[:5],
                                          chat_id=query.message.chat_id,
                                          message_id=query.message.message_id)
    else:
        bot.edit_message_text(text="Under Construction",
                                          chat_id=query.message.chat_id,
                                          message_id=query.message.message_id)

updater.dispatcher.add_handler(CommandHandler('startkey', startKey))
updater.dispatcher.add_handler(CallbackQueryHandler(button))


updater.start_polling()