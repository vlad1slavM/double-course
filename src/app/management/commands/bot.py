from django.core.management.base import BaseCommand
from app.internal.transport.for_bot.handlers import start_bot


class Command(BaseCommand):
    help = 'Telegram for_bot'

    def handle(self, *args, **options):
        start_bot()
