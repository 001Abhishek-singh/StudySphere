from django.shortcuts import render

# Create your views here.
def Assignments(request):
    return render(request,'assignment.html',{})