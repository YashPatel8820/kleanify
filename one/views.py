# from django.http.response import HttpResponse
# from django.shortcuts import render, redirect
# from refer.models import *
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import  login, authenticate
# from django.contrib.auth.models import User 

# ############ // Page showed by referral link \\ #######################
# def signup_view(request,*args, **kwargs):
#     profile_id = request.session.get('ref_profile')
#     print("profile_id", profile_id)
#     form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#         if profile_id is not None:
#             recommended_by_profile = Profile.objects.get(id = profile_id)
#             instance = form.save()
#             registered_user = User.objects.get(id = instance.id)
#             registered_profile = Profile.objects.get(user = registered_user)
#             registered_profile.recommended_by = recommended_by_profile.user
#             registered_profile.save()
#         else:
#             form.save()

#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username = username, password = password)
#         # login(request, user)
#         return redirect('main')
    
#     context = {'form': form}
#     return render(request, 'signup.html', context)


# ############ // Page showed by referral link \\ #######################
# def main_view_one(request, *args, **kwargs):
#     code = str(kwargs.get('ref_code'))
#     try:
#         profile = Profile.objects.get(code = code)
#         request.session['ref_profile'] = profile.id
#         xxx = profile.user
#         print("id", profile.id)
#     except:
#         pass
#     print(request.session.get_expiry_age())
#     return render(request, 'main.html', {"x" : xxx})



# ############ // Mainadmin logged in user \\ #######################
# # def main_view(request, *args, **kwargs):
# #     code = str(kwargs.get('ref_code'))
# #     try:
# #         profile = Profile.objects.get(code = code)
# #         request.session['ref_profile'] = profile.id
# #     except:
# #         pass
# #     print(request.session.get_expiry_age())
# #     return render(request, 'adminview.html')


# def main_view(request, *args, **kwargs):
#     code = str(kwargs.get('ref_code'))
#     try:
#         profile = Profile.objects.get(code=code)
#         request.session['ref_profile'] = profile.id
#         print('id', profile.id)
#     except:
#         pass
#     print(request.session.get_expiry_age())
#     return render(request, 'adminview.html', {})

# # def ss(request, *args, **kwargs):
# #     code = str(kwargs.get('ref_code'))
    
# #     profile = Profile.objects.get(code = code)
# #     request.session['ref_profile'] = profile.id
# #     print(profile.user)
# #     print("id", profile.id)  


# # def child_view(request,ref_code,*args, **kwargs):
# #     code = str(kwargs.get('ref_code'))
# #     try:
# #         pro = Profile.objects.get(code = code)
# #         x = Profile.objects.get(ref_code)
# #         for i in x:
# #             print(i)
# #         request.session['ref_profile'] = pro.id
# #         # print("id", profile.id)
# #     except:
# #         pass

# #     return render(request, 'main.html')