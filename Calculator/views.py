from django.shortcuts import render

# Create your views here.
def Calculator(request):
    return render(request,'calculator.html',{})