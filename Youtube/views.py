from django.shortcuts import render

# Create your views here.
def Youtube(request):
    return render(request,'youtube.html',{})