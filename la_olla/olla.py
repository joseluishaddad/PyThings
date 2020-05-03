#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Bot simple para jugar a la olla online.
Por ahora asume que los jugadores no hacen trampa y requiere reiniciarse cada vez que se acaban las palabras.
Además no tiene forma aún de volver meter palabras inválidas a la lista.
"""

import logging
import os
import json

import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola! Vamos a jugar a la olla')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(" \
        Envía el comando /turno para recibir una palabra.")

def turno(update, context):
    """Get split preferences."""
    global palabras
    if len(palabras) == 0:
        update.message.reply_text("SE ACABARON LAS PALABRAS")
    else:
        rand = random.randint(0, len(palabras)-1)
        update.message.reply_text(palabras.pop(rand))

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(f"No entendí eso {update.message.chat.first_name}...")

def error(update, context):
    """Log Errors caused by Updates."""
    update.message.reply_text(f'Whoops, wrong input! {context.chat_data.get("last_exception", "")} Try again ;)')
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(<token>, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("turno", turno))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    palabras = ["She's got a smile that it seems to me", "Reminds me of childhood memories", "Where everything was as fresh as the bright blue sky", "Now and then when I see her face", "She takes me away to that special place", "And if I stare too long, I'd probably break down and cry"]
    main()

