from django.shortcuts import render

# Create your views here.
def Dictionary(request):
    return render(request,'dictionary.html',{})