"""one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from refer.views import *
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', include('first.urls')),
    path('fire/', include('firebasetest.urls')),
    path('filter/', include('filter_test.urls')),
    path('test/', include('borb_test.urls')),
    path('refer/', include('refer.urls')),
    # path('ca/', include('CA.urls')),
    # path('<str:ref_code>/', PRSignupView, name='PRSIGNUPVIEW'),
    path('api-auth/', include('rest_framework.urls')),


   # path('abc/<str:ref_code>', child_view, name = 'child-view'),
# path("profiles/", my_recommendations_view, name = "my-recs-view"),

    # path('', main_view, name = 'main'), # Done
    # path('<str:ref_code>', main_view_one), #Done
    # path('signup/', signup_view, name = 'signup-view'),  #DONE
    # path("profiles/<str:ref_code>", my_recommendations_view_one, name = "my-recs-view") #Done

    # path('hh/', views.home),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)