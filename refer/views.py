from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from refer.forms import RegisterForm, choiceForm
from refer.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  login, authenticate
from django.contrib.auth.models import User 
from django.http import HttpResponse,Http404
from first.serializers import *
from rest_framework import views
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.conf import settings
from refer.serializers import *
import netifaces 
import requests
import socket

# Create your views here.



############ // Page showed by referral link \\ #######################
def signup_view(request,*args, **kwargs):
    profile_id = request.session.get('ref_profile')
    print("profile_id", profile_id)
    form = choiceForm(request.POST or None)
    nform = RegisterForm(request.POST)
    if nform.is_valid() :
        if profile_id is not None:
            recommended_by_profile = Profile.objects.get(id = profile_id)
            instance = nform.save()
            registered_user = User.objects.get(id = instance.id)
            registered_profile = Profile.objects.get(user = registered_user)
            registered_profile.recommended_by = recommended_by_profile.user
            registered_profile.save()
        else:
            nform.save()
        username = nform.cleaned_data.get('username')
        password = nform.cleaned_data.get('password1')
        user = authenticate(username = username, password = password)

       
        if form.is_valid():
            eee = form.cleaned_data['eee']
            m = Profile.objects.latest('id')
            if eee == 'false':
                m.identify = bool(False)
            elif eee == 'true':
                m.identify = bool(True)
            elif eee == 'none':
                m.identify = None
            m.save()

        xyz = Profile.objects.latest('id')
        try:
            fin = requests.get("https://api6.ipify.org", timeout=5).text
            xyz.ip = fin
            xyz.update()
        except requests.exceptions.ConnectionError as ex:
            print(None)

        # xyz = Profile.objects.latest('id')
        # print(xyz)
        # interface = netifaces.interfaces()
        # print(interface)
        # int = interface[1]
        # addrs = netifaces.ifaddresses(int)
        # x = addrs.get(10)
        # global_add = x[0].get('addr')
        # print(global_add)
        # link_local = x[2].get('addr')
        # link_local = link_local.replace("%enp8s0","" )
        # print(link_local)
        # final_add = global_add +":"+ link_local
        # xyz.ip = final_add 
        # xyz.save()

            
            
        # login(request, user)
        return redirect('main')
    
    context = {'nform': nform, 'form' : form}
    return render(request, 'signup.html', context)


############ // Page showed by referral link \\ #######################
def main_view_one(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code = code)
        request.session['ref_profile'] = profile.id
        xxx = profile.user
        print("id", profile.id)
    except:
        pass
    print(request.session.get_expiry_age())
    return render(request, 'main.html', {"x" : xxx})



############ // Mainadmin logged in user \\ #######################
# def main_view(request, *args, **kwargs):
#     code = str(kwargs.get('ref_code'))
#     try:
#         profile = Profile.objects.get(code = code)
#         request.session['ref_profile'] = profile.id
#     except:
#         pass
#     print(request.session.get_expiry_age())
#     return render(request, 'adminview.html')


def main_view(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
        print('id', profile.id)
    except:
        pass
    print(request.session.get_expiry_age())
    return render(request, 'adminview.html', {})

# def ss(request, *args, **kwargs):
#     code = str(kwargs.get('ref_code'))
    
#     profile = Profile.objects.get(code = code)
#     request.session['ref_profile'] = profile.id
#     print(profile.user)
#     print("id", profile.id)  


# def child_view(request,ref_code,*args, **kwargs):
#     code = str(kwargs.get('ref_code'))
#     try:
#         pro = Profile.objects.get(code = code)
#         x = Profile.objects.get(ref_code)
#         for i in x:
#             print(i)
#         request.session['ref_profile'] = pro.id
#         # print("id", profile.id)
#     except:
#         pass

#     return render(request, 'main.html')

def my_recommendations_view_one(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    
    profile = Profile.objects.get(code = code)
    request.session['ref_profile'] = profile.id
    nam = profile.user
    print("id", profile.id)
    
    # profile = Profile.objects.get('ref_code')
    my_recs = profile.get_recommend_profiles()
    context = {'my_recs' : my_recs, 'n' : nam}
    return render(request, 'alag.html', context)



######################## // API Code \\ ###########################

class Allview(APIView):
    def get(self, request):
        queryset = Profile.objects.all()
        print(queryset)
        serializer = AllSerializer(queryset, many = True)
        return Response(serializer.data)

# class Addview(APIView):
#     serializer_class = AddSerializer

#     def get(self, request):
#         queryset = Profile.objects.all()
#         serializer = AllSerializer(queryset, many = True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = self.serializer_class(data = request.data)
#         serializer.is_valid()
#         serializer.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)

