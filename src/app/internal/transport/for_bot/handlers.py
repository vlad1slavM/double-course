from django.conf import settings
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, ConversationHandler

from app.internal.transport.bot_main import me, set_phone, start, phone, cancel


def start_bot():
    updater = Updater(token=settings.TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    me_handler = CommandHandler('me', me)
    set_phone_handler = ConversationHandler(
        entry_points=[CommandHandler('set_phone', set_phone)],
        states={
            0: [MessageHandler(Filters.text & ~Filters.command, phone)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(start_handler)

    dispatcher.add_handler(set_phone_handler)
    dispatcher.add_handler(me_handler)
    updater.start_polling()
    updater.idle()
