from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from app.internal.services.user_service import get


def echo(request):
    if request.method == 'GET':
        tg_id = request.GET.get('tg_id')
        user_created, user = get(tg_id)

        if user_created:
            return HttpResponse(f'Name: {user.first_name} <br>'
                                f'SurName: {user.last_name} <br>'
                                f'PhoneNumber: {user.phoneNumber}', status=200)
        else:
            return HttpResponse(f'Does not exist', status=403)
    else:
        return HttpResponse(f"Not right type of response", status=405)
