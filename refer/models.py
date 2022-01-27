from django.db import models
from django.contrib.auth.models import User    
from .utils import *
# Create your models here.


# class Recognize(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     rec = models.BooleanField()

#     def __str__(self):
#         return str(self.rec)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=55, default="")
    identify = models.BooleanField(default=False, null=True)
    ip = models.CharField(max_length=100,default='', blank=True, null=True)


    def __str__(self):
        if self.recommended_by == None :
            return f"{self.user}-{self.code}-{'main'}"
        elif self.identify == bool(True):
            return f"{self.user}-{self.code}-{'CA'}"
        elif self.identify == bool(False):
            return f"{self.user}-{self.code}-{'Promoter'}"
        else:
            return f"{self.user}-{self.code}-{'user'}"




    def get_recommend_profiles(self):
        qs = Profile.objects.all()
        my_recs = []
        for profile in qs:
            if profile.recommended_by == self.user:
                my_recs.append(profile)
        return my_recs

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
        
        self.link = "http://127.0.0.1:8000/refer/" + str(self.code)
        super().save(*args, **kwargs)

    