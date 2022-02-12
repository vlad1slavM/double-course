import re
from django.core.exceptions import ObjectDoesNotExist
import environ
import os

from app.models import User

env = environ.Env(
    TOKEN=(str, ''),
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, 'envs/.env'))

TOKEN = env('TOKEN')


def start(update, context):
    tg_id = update.message.from_user.id
    chat_id = update.effective_chat.id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    p, created = User.objects.get_or_create(
        tg_id=tg_id,
        defaults={
            'username': username,
            'first_name': first_name,
            'last_name': last_name
        }
    )
    if created is False:
        context.bot.send_message(chat_id=chat_id,
                                 text='Такой пользователь уже создан')
    else:
        context.bot.send_message(chat_id=chat_id,
                                 text=
                                 f'Я создал пользователя: \n'
                                 f'С именем: {first_name} \n'
                                 f'С фамилией: {last_name} \n'
                                 f'Вы так же можете добавить номер телефона с помощью команды: \n'
                                 f'/set_phone'
                                 )


def set_phone(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Напишете свой номер телефона в формате +7")


def me(update, context):
    tg_id = update.message.from_user.id
    chat_id = update.effective_chat.id
    try:
        user = User.objects.get(tg_id=tg_id)
        if len(user.phoneNumber) == 0:
            context.bot.send_message(chat_id=chat_id,
                                     text='Добавьте номер телефона с помощью команды:\n'
                                          '/set_phone')
        else:
            context.bot.send_message(chat_id=chat_id,
                                     text=f'Ваше имя: {user.first_name} \n'
                                          f'Ваша фамилия: {user.last_name} \n'
                                          f'Ваш номер телефона: {user.phoneNumber}')
    except ObjectDoesNotExist:
        context.bot.send_message(chat_id=chat_id,
                                 text='Сначала добавьте свои данные в базу данных \n'
                                      'С помощью команды /start \n'
                                      'А так же не забудьте добавить свой номер телефона с помощью команды /set_phone')


def on_message(update, context):
    text = update.message.text
    tg_id = update.message.from_user.id
    chat_id = update.effective_chat.id
    try:
        User.objects.get(tg_id=tg_id)
    except ObjectDoesNotExist:
        context.bot.send_message(chat_id=chat_id,
                                 text='Вомрользуйтесь командой /start')
        return 1

    if re.match(r'^\+?1?\d{8,15}$', text) is None and len(text) < 10:
        context.bot.send_message(chat_id=chat_id,
                                 text='Пожалуйста, введите номер телефона')
    else:
        p, _ = User.objects.update_or_create(
            tg_id=tg_id,
            defaults={
                'phoneNumber': str(text)
            }
        )

        context.bot.send_message(chat_id=chat_id,
                                 text='Ваш номер был успешно добавлен')
