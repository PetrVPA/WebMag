
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),#пути в адресной строке
    path("home/", views.home),
    path("contacts/", views.contacts),
]
