from django.urls import path

from .transport.rest.handlers import get_info_about_user

urlpatterns = [
    path("me", get_info_about_user),
]
