import re
from enum import Enum

from app.internal.services.user_service import create_user, get, update_info


class HandlerStates(Enum):
    PHONE = 0
    EXIT = -1


def validate_user(func):
    def wrapper(*args, **kwargs):
        tg_id = args[0].message.from_user.id
        chat_id = args[0].effective_chat.id
        user_created, _ = get(tg_id)
        if user_created:
            return func(*args)
        else:
            args[1].bot.send_message(chat_id=chat_id,
                                     text='Сначала воспользуйтесь командой /start')

    return wrapper


def validate_phone_number(func):
    def wrapper(*args, **kwargs):
        tg_id = args[0].message.from_user.id
        chat_id = args[0].effective_chat.id
        user_created, user = get(tg_id)
        if user_created:
            if len(user.phoneNumber) == 0:
                args[1].bot.send_message(chat_id=chat_id,
                                         text='Добавьте номер телефон с помощью команды /set_phone')
            else:
                return func(*args)
        else:
            args[1].bot.send_message(chat_id=chat_id,
                                     text='Сначала воспользуйтесь командой /start')

    return wrapper


def start(update, context):
    tg_id = update.message.from_user.id
    chat_id = update.effective_chat.id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    created = create_user(tg_id, username, first_name, last_name)
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


@validate_user
def set_phone(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Напишете свой номер телефона в формате +7")
    return HandlerStates.PHONE.value


def phone(update, context):
    text = update.message.text
    tg_id = update.message.from_user.id
    chat_id = update.effective_chat.id

    if re.match(r'^\+?1?\d{8,15}$', text) is None and len(text) < 10:
        context.bot.send_message(chat_id=chat_id,
                                 text='Это не номер телефона\n'
                                      'Если хотите завершить ввод введите /cancel')
        return HandlerStates.PHONE.value

    else:
        update_info(tg_id, text)
        context.bot.send_message(chat_id=chat_id,
                                 text='Ваш номер был успешно добавлен')
        return HandlerStates.EXIT.value


def cancel(update, context):
    return -1


@validate_phone_number
def me(update, context):
    tg_id = update.message.from_user.id
    chat_id = update.effective_chat.id
    user_created, user = get(tg_id)
    context.bot.send_message(chat_id=chat_id,
                             text=f'Ваше имя: {user.first_name} \n'
                                  f'Ваша фамилия: {user.last_name} \n'
                                  f'Ваш номер телефона: {user.phoneNumber}')
