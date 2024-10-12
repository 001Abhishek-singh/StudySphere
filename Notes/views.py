from django.shortcuts import render,redirect
def notes(request):
    return render(request,'notes.html',{})