from django.shortcuts import render
from .models import Dictionary
import requests
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='loginAccount')
def DictionaryWord(request):
    if request.method == 'POST':
        inputword = request.POST['dictionary']
        Dict_obj = Dictionary(word=inputword)
        Dict_obj.save()

        # calling dictionary api
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{inputword}'
        res = requests.get(url)
        json_data = res.json()

        try:
            phonetics = json_data[0]['phonetics'][0]['text']
            audio = json_data[0]['phonetics'][0]['audio']
            definition = json_data[0]['meanings'][0]['definitions'][0]['definition']
            example = json_data[0]['meanings'][0]['definitions'][0]['example']
            synonyms = json_data[0]['meanings'][0]['definitions'][0]['synonyms']

            context = {
                'inputword': inputword,
                'phonetics': phonetics,
                'audio': audio,
                'definition': definition,
                'example': example,
                'synonyms': synonyms 
            }
        except:
            context = {
                'input': 'something wrong'
            }
        return render(request,'dictionary.html',context)

    return render(request,'dictionary.html',{})