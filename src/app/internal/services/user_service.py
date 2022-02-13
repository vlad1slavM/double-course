from app.models import User


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
    user = User.objects.get(tg_id=tg_id)
    return user


def update_info(tg_id, phone_number):
    User.objects.update_or_create(
        tg_id=tg_id,
        defaults={
            'phoneNumber': str(phone_number)
        }
    )
