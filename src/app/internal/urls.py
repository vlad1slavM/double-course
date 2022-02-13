from django.urls import path
from .transport.rest.handlers import echo

urlpatterns = [
    path("me/", echo),
]
