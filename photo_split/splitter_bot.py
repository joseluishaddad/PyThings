#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import splitter
import os
import json

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi, I am the splitter bot and I can split your photos!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(" \
        You can send me a picture not larger than 20MB and the send the splitting details by doing\n\n/split <n> <axis>\n\nwhere 'n' is the number of split and 'axis' is either x or y.")

def split(update, context):
    """Get split preferences."""
    command_args = update.message.text.split()
    n_split = int(command_args[1])
    axis_split = command_args[2].lower()
    if n_split <= 0:
        context.chat_data["last_exception"] = f"'{n_split}' is not a valid number of splits."
        raise Exception
    if axis_split not in ['x', 'y']:
        context.chat_data["last_exception"] = f"'{axis_split}' is not a valid axis."
        raise Exception
    # Save it within the context
    context.chat_data['n'] = n_split
    context.chat_data['axis'] = axis_split
    update.message.reply_text(f"Your image will be splitted in {n_split} parts in the {axis_split} axis.")
    
    if context.chat_data.get('img_received', False):
        split_and_send(update, context)
    else:
        update.message.reply_text("Now send me a picture!")

def split_and_send(update, context):
    splitter.split(n=context.chat_data['n'], split_axis=context.chat_data['axis'])
    for filename in os.listdir("output"):
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'output/{filename}', 'rb'))
        os.remove(f'output/{filename}')
    os.remove('input/input_img.jpg')
    
    # Reset parameters stored
    context.chat_data['n'] = False
    context.chat_data['axis'] = False
    context.chat_data['img_received'] = False

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(f"What do you mean {update.message.chat.first_name}?")

def save_photo(update, context):
    """Echo the user message."""
    file_id = update.message.photo[-1]
    newFile = context.bot.get_file(file_id)
    newFile.download('input/input_img.jpg')
    context.chat_data['img_received'] = True
    update.message.reply_text("I received your picture!")

    if context.chat_data.get('n', False):
        split_and_send(update, context)
    else:
        update.message.reply_text("Now send me the split parameters!")

def error(update, context):
    """Log Errors caused by Updates."""
    update.message.reply_text(f'Whoops, wrong input! {context.chat_data.get("last_exception", "")} Try again ;)')
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.getenv('TELEGRAM_TOKEN'), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("split", split))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.photo, save_photo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()