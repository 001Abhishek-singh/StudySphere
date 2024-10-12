from django.shortcuts import render

# Create your views here.
def Wikipedia(request):
    return render(request,'wikipedia.html',{})