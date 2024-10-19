from django.shortcuts import render
from .models import WikipediaList
import wikipedia
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='loginAccount')
def wikipediafun(request):
    if request.method == 'POST':
        textInput = request.POST['wikipedia']
        wiki_obj = WikipediaList(input = textInput)
        wiki_obj.save()
        search = wikipedia.page(textInput)
        context = {
            'title':search.title,
            'link':search.url,
            'details':search.summary,
            'content':search.content
        }
        return render(request,'wikipedia.html',context)
    else:
        return render(request,'wikipedia.html',{})