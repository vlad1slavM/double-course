from app.models import User
from django.core.exceptions import ObjectDoesNotExist


def create_user(tg_id, username, first_name, last_name):
    p, created = User.objects.get_or_create(
        tg_id=tg_id,
        defaults={
            'username': username,
            'first_name': first_name,
            'last_name': last_name
        }
    )

    return created


def get(tg_id):
    try:
        user = User.objects.get(tg_id=tg_id)
        user_created = True
    except ObjectDoesNotExist:
        user_created = False
        user = False

    return user_created, user


def update_info(tg_id, phone_number):
    User.objects.update_or_create(
        tg_id=tg_id,
        defaults={
            'phoneNumber': str(phone_number)
        }
    )
