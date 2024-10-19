from django.shortcuts import render
from .models import Assignments
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='loginAccount')
def useAssignment(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['shortDesc']
        location = request.POST['location']
        date = request.POST['date']
        introduction = request.POST['introduction']
        content = request.POST['content']
        conclusion = request.POST['conclusion']

        obj = Assignments(title=title,description=description,location=location,date=date,introduction=introduction,content=content,conclusion=conclusion)
        obj.save()
        print(title,description, location)

    Dict_obj = Assignments.objects.all()
    dict = {'Dict_obj':Dict_obj}
    return render(request,'assignment.html',{})

def AddAssignment(request):

    Dict_obj = Assignments.objects.all()
    dict = {'Dict_obj':Dict_obj}
    return render(request,'assignmentResult.html',dict)