from django.shortcuts import render

# Create your views here.
def CheckWeather(request):
    return render(request,'weather.html',{})