from django.contrib import admin
from django.urls import path, include
from firebasetest.views import *


urlpatterns = [
    path('h/', index),

]
