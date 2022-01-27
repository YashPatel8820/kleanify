from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib import admin
from rest_framework import fields
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.admin.site.register(Profile)

admin.site.register(Profile)
# admin.site.register(Recognize)

# class RecognizeInline(admin.StackedInline):
#     model = Recognize
#     # fields = ['recommended_by']
#     can_delete = False
#     verbose_name_plural = 'Recommended'
    
# class CustomizeUserAdmin (UserAdmin):
#     inlines = (RecognizeInline,)

# admin.site.unregister(User)
# admin.site.register(User,CustomizeUserAdmin)


