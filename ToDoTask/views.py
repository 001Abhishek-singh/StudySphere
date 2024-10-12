from django.shortcuts import render

# Create your views here.
def ToDoTask(request):
    return render(request,'todo.html',{})