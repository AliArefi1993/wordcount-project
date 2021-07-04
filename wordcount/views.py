import operator
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    fulltext = fulltext.lower()
    for ch in '!"#$%()*+,-. /:;<=>?@[\\]^_`{|}-':
        fulltext = fulltext.replace(ch, ' ')
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        worddictionary[word] = worddictionary.get(word,0) + 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),
                  'sortedwords':sortedwords})
def about(request):
    return render(request,'about.html')