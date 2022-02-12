from django.http import HttpResponse
from app.models import User
from django.core.exceptions import ObjectDoesNotExist


def echo(request):
    tg_id = request.GET.get('tg_id')
    try:
        user = User.objects.get(
            tg_id=tg_id,
        )
        return HttpResponse(f'Name: {user.first_name} <br>'
                            f'SurName: {user.last_name} <br>'
                            f'PhoneNumber: {user.phoneNumber}', status=200)
    except ObjectDoesNotExist:
        return HttpResponse(f'Does not exist', status=404)
