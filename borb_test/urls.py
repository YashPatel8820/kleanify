from django.contrib import admin
from django.urls import path, include
from borb_test.views import *

urlpatterns = [
    path('e1/', ext)
]