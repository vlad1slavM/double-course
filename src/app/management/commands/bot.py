from django.core.management.base import BaseCommand, no_translations
from telegram.ext import CommandHandler, Updater, Filters, MessageHandler

from app.management.bot_main import start, set_phone, me, on_message
from django.conf import settings


class Command(BaseCommand):
    help = 'Telegram bot'

    @no_translations
    def handle(self, *args, **options):
        updater = Updater(token=settings.TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        start_handler = CommandHandler('start', start)
        set_phone_handler = CommandHandler('set_phone', set_phone)
        me_handler = CommandHandler('me', me)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(set_phone_handler)
        dispatcher.add_handler(me_handler)
        dispatcher.add_handler(MessageHandler(Filters.all, on_message))
        updater.start_polling()
        updater.idle()
