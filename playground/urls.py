from django.urls import path
from . import views

urlpatterns = [
    path('playground/hwllo', views.say_hello)
]
