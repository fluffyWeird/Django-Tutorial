from django.shortcuts import render
import operator
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request,"about.html")
def count(request):
    fullText=request.GET['fullText']
    newText=fullText.split()
    count=len(newText)
    sortedText=sorted(newText)
    wordDictionary={}
    for word in sortedText:
        if word in wordDictionary:
            wordDictionary[word] +=1
        else:
            wordDictionary[word]=1
    print(wordDictionary)

    return render(request,"count.html", {'count':count, 'wordDictionary':wordDictionary})
