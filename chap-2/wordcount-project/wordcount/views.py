from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'index.html')
    
def count(request):
    fulltext = request.GET['fulltext'] 
    wordlist=fulltext.split()
    sortedwordlist=sorted(wordlist)
    print(sortedwordlist)
    wordanalyser={}
    for word in sortedwordlist:
        if word in wordanalyser:
            wordanalyser[word]+=1
        else:
            wordanalyser[word]=1
    print(wordanalyser)
             
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'wordanalyser':wordanalyser})
def about(request):
    return render(request, 'about.html')