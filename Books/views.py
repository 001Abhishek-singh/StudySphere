from django.shortcuts import render
from .models import Books
import requests
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='loginAccount')
def books(request):
    if request.method == 'POST':
        bookInput = request.POST['books']
        books_obj = Books(input=bookInput)
        books_obj.save()
        # adding api so that we can get the books from google playbook
        url = 'https://www.googleapis.com/books/v1/volumes?q='+bookInput
        res = requests.get(url)
        # store the json value in answer variable
        answer = res.json()
        # creating an empty list so that we can store the instances of the books
        result_list = []
        for i in range(10):
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating': answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail': answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview': answer['items'][i]['volumeInfo'].get('previewLink')
            }
            result_list.append(result_dict)
            booklist = {
                'results':result_list
            }
        return render(request,'youtube.html',booklist)
    return render(request,'books.html',{})