from django.shortcuts import render
from .models import YoutubeInput
from youtubesearchpython import VideosSearch
# Create your views here.
def Youtube(request):
    if request.method == "POST":
        youtube = request.POST['youtube']
        youtube_obj = YoutubeInput(input=youtube)
        youtube_obj.save()
        video = VideosSearch(youtube,limit=12,language='en')
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input': youtube,
                'title': i['title'],
                'duration': i['duration'],
                'thumbnail': i['thumbnails'][0]['url'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'views': i['viewCount']['short'],
                'published': i['publishedTime']
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)

            dictlist = {
                'results':result_list
            }
        return render(request,'youtube.html',dictlist)
        # youtube_obj = YoutubeInput(input=youtube)
        # youtube_obj.save()
    
    return render(request,'youtube.html',{})