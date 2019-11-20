from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    worddict = {}

    for word in words:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    return render(request, 'count.html',{'fulltext': fulltext,'count':len(words),'worddict':worddict.items })

def about(request):
    return render(request, 'about.html')