from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from refer.views import *

urlpatterns = [
    path('', main_view, name = 'main'), # Done
    path('<str:ref_code>', main_view_one), #Done
    path('signup/', signup_view, name = 'signup-view'),  #DONE
    path("profiles/<str:ref_code>", my_recommendations_view_one, name = "my-recs-view"), #Done



    ################## // API\\ ##################
    # path('all/', Allview.as_view()),
    # path('add/', Addview.as_view()),



]