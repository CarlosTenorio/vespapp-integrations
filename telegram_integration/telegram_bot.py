import threading, time

from telegram import Updater
from telegram_integration.telegram_keys import TelegramKeys
from telegram_integration.telegram_photo import TelegramPhoto
from telegram_integration.telegram_location import TelegramLocation
from telegram_integration.telegram_requester import TelegramRequester

# global variables
keys = TelegramKeys()

# create bot
updater = Updater(token='175120475:AAGxpJ4TC-24XTF6Jvub9-eWYEqQFJ0AUZo')
dispatcher = updater.dispatcher


#                  #
# main definitions #
#                  #

# start definition (cmd: /start)
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hola, ¿Podrías mandarnos una foto y la localización?")

# add /start dispatcher
dispatcher.addTelegramCommandHandler('start', start)


# echo definition (send any message data)
def echo(bot, update):
    if TelegramPhoto.is_photo(update):
        # add photo in keys
        file_id = TelegramPhoto.get_file_id(update)
        result = keys.add_photo(chat_id=update.message.chat_id, file_id=file_id)
        if not result:
            # create thread
            thr = threading.Thread(target=time_out, args=[bot, update.message.chat_id])
            thr.start()

        # image received
        if 'location' not in keys.get_key_by_id(update.message.chat_id):
            bot.sendMessage(chat_id=update.message.chat_id, text="Imagen recibida! Gracias por tu colaboración! ¿Podrías mandarnos la localización?")
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text="Imagen recibida! Gracias por tu colaboración!")
        # TODO send custom keyboard

    elif TelegramLocation.is_location(update):
        # get latitude and longitude
        latitude, longitude = TelegramLocation.get_location(update)
        # add location in keys
        result = keys.add_location(chat_id=update.message.chat_id, latitude=latitude, longitude=longitude)
        if not result:
            # create thread
            thr = threading.Thread(target=time_out, args=[bot, update.message.chat_id])
            thr.start()

        # location received
        if 'photos' not in keys.get_key_by_id(update.message.chat_id):
            bot.sendMessage(chat_id=update.message.chat_id, text="Localización recibida! Gracias por tu colaboración! ¿Podrías enviarnos una foto?")
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text="Localización recibida! Gracias por tu colaboración!")
        # TODO send custom keyboard

    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Gracias, pero no es ni una foto ni una localización")

# add echo to dispatcher
dispatcher.addTelegramMessageHandler(echo)

# start bot #
updater.start_polling()

#                   #
# other definitions #
#                   #

# define time out function (threading)
def time_out(bot, chat_id):
    # config time expiration
    time.sleep(150)
    keys.add_type(chat_id=chat_id, type=0)
    TelegramRequester.send_request(bot=bot, key=keys.get_key_by_id(chat_id))
    keys.remove_key(chat_id)
    bot.sendMessage(chat_id=chat_id, text="Hemos registrado su avispamiento!")
    bot.sendMessage(chat_id=chat_id, text="Gracias por la colaboración!")

