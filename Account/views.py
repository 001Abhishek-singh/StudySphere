from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def registrationpage(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirm_password']

        if password == confirmPassword:
            profile_obj = UserProfile(name=name, email=email, password=password, confirmPassword=confirmPassword)
            profile_obj.save()
            UserObj = User.objects.create_user(username=profile_obj.name, email=profile_obj.email, password=profile_obj.password)
            UserObj.save()
            # UserObj = User.objects.create_user(username=name, email=email, password=password)
            # UserObj.save()

            messages.info(request,'Registration Successfull')
            return redirect('loginAccount')
        else:
            messages.info(request,'Please confirm your Password')
    return render(request,'index.html',{})    

def loginAccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        authuser = authenticate(request, username=username, password = password)
        if authuser is not None:
            login(request,authuser)
            return redirect('home')
        else:
            messages.warning(request,'Please check your credentials')
    return render(request,'index.html',{})

@login_required(login_url='loginAccount')
def Homepage(request):
    return render(request, 'home.html',{})

def logoutpage(request):
    logout(request)
    return redirect('loginAccount')
