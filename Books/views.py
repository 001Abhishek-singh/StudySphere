from django.shortcuts import render

# Create your views here.
def Books(request):
    return render(request,'books.html',{})