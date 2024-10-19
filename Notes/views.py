from django.shortcuts import render,get_object_or_404,redirect
from .models import Notes
from django.contrib.auth.decorators import login_required
@login_required(login_url='loginAccount')
def addNotes(request):
    # getting the values from the input form
    if request.method == 'POST':
        subject = request.POST['subject']
        topic = request.POST['topic']
        date = request.POST['date']
        description = request.POST['description']

        # assigning the values to the given model
        obj = Notes(subject=subject,topic=topic,date=date,description=description) 
        obj.save()
    
    notesdict = Notes.objects.all()

    user = 'Abhishek'
    # creating an object and assigning the values to the given notes.html file
    dictionary = {
        'notesdict':notesdict,
        'user':user,
    }
    return render(request,'notes.html',dictionary)

def updateNotes(request,Notes_Id):
    # Retrieve the Notes object or return 404 if not found
    updateObj = get_object_or_404(Notes, id=Notes_Id)
    print(type(Notes_Id))
    if request.method == 'POST':
        updateObj.topic = request.POST['topic']
        updateObj.date = request.POST['date']
        updateObj.description = request.POST['description']
        updateObj.save()

    updateDic = {
        'updateObj':updateObj
    }
    return render(request,'updateNotes.html',updateDic)

def deleteNotes(request,Notes_Id):
    # Retrieve the Notes object or return 404 if not found
    deleteObj = get_object_or_404(Notes, id=Notes_Id)
    deleteObj.delete()
    return redirect('/add/notes/')


