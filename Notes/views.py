from django.shortcuts import render,redirect
from .models import Notes
def addnotes(request):
    notes_obj = Notes.objects.all()
    print(notes_obj)
    # this method is used to add the data in a given database
    if request.method == 'POST':
        subject = request.POST['subject']
        topic = request.POST['topic']
        date = request.POST['date']
        description = request.POST['note']

        notes_obj = Notes(subject=subject,topic=topic,date=date,notes=description,user=request.user)
        notes_obj.save()
        print(subject,topic,date)

    return render(request,'notes.html', {'notesObj': notes_obj})

def deleteNote(request,ID):
    Notes.objects.get(id=ID).delete()
    # return redirect('add/notes/')
    return render(request,'notes.html',{})