# import uuid
from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib import messages
# from .models import Profile
# from django.conf import settings
# from django.core.mail import send_mail
# from django.core.mail import EmailMessage
# from django.contrib.auth import authenticate,login
# from django.contrib.auth.decorators import login_required

def loginAccount(request):
    return render(request,'index.html',{})

def home(request):
    return render(request,'home.html',{})

# def notes(request):
#     return render(request,'notes.html',{})
# def mail_send(email, token):
#     subject='Account Verification'
#     message = f"Click on this link to verify your email account http://127.0.0.1:8789/verify/{token} "
#     email_from = settings.EMAIL_HOST_USER 
#     recipient_list = [email]  
#     send_mail(subject,message,email_from,recipient_list) 

# # def index(request):
# #     return render(request,'index.html',{})

# def registerAccount(request):
#     if request.method == 'POST':
#         firstname = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         print(firstname, email, password,confirm_password)
#         print(str(uuid.uuid4()))

#     try:
            
#         if User.objects.filter(username=firstname).exists():
#             messages.info(request, "User is already created")
#             return redirect('/loginAccount/')
        
#         if User.objects.filter(email = email).exists():
#             messages.info(request, "Email is already taken")
#             return redirect('/loginAccount/')
        
#         else:
#             user_obj = User.objects.create_user(username=firstname, email=email, password = password)
#             user_obj.save()
#             auth_token = str(uuid.uuid4())
#             user_profile_obj = Profile(user=user_obj, auth_token=auth_token)
#             user_profile_obj.save()
#             mail_send(email, auth_token)
#         return redirect('/checkemail/')

#     except Exception as e:
#         print(e)
#     return render(request,'index.html',{})

# @login_required(login_url='/')
# def loginAccount(request):
#     if request.method == 'POST':
#         # useremail = request.POST.get('useremail')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username,password)
#         # to check email exist in the User database or not
#         user_obj = User.objects.filter(username = username).first()

#         if not user_obj:
#             messages.info(request,'User not found')
#             # print(user_obj)
#             return redirect('/')
        
#         # to check email is verified or not
#         profile_obj = Profile.objects.filter(user = user_obj).first()
#         if not profile_obj.is_valid:
#             messages.info(request,'Email is not verified check your mail')
#             # print(profile_obj)
#             return redirect('/')

#         user_auth = authenticate(request,username=username, password = password)
#         if user_auth is not None:
#             login(request,user_auth)
#             return redirect('/home/')
#         else:
#             messages.info(request,'Username or Password is Incorrect')
#             return redirect('/')
#     return render(request,'index.html',{})
        
# def verify_email(request, auth_token):
#     try:
#         profile_user_obj = Profile.objects.filter(auth_token = auth_token).first()
#         if profile_user_obj:
#             if profile_user_obj.is_valid:
#                 messages.success(request,'Your account has been already verified.')
#                 return redirect('/')
            
#             profile_user_obj.is_valid = True
#             profile_user_obj.save()
#             messages.success(request,"Congratulations!!! your account has been verified successfully.")
#             return redirect('/')
#         else:
#             return redirect('/error')
        
#     except Exception as e:
#         print(e)
    
#     return HttpResponse("Something went wrong")

# def checkemail(request):
#     return render(request,'checkemail.html',{})

# def error(request):
#     return render(request, 'error.html', {})

# def home(request):
#     return render(request,'home.html')

