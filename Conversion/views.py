from django.shortcuts import render

# Create your views here.
def Conversion(request):
    return render(request,'conversion.html',{})