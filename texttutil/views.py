# This is my Site
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def about(request):
    djtext = request.POST.get('text' , 'default')
    removepunch = request.POST.get('removepunc' , 'off')
    uppercase = request.POST.get('uppercase' , 'off')
    charcount = request.POST.get('charcount' , 'off')
    newlineremover = request.POST.get('newlineremover' , 'off')

    if removepunch == "on":
        punctuations ='''"#$%&'()*+,-./:;<=>?@[\]^_`{|}~!'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        shree = {'purpose': 'Removed punchations' ,'after_operation': analyzed}
        djtext = analyzed

    if(uppercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        shree = {'purpose': 'Your uppercase Latter' ,'after_operation': analyzed}
        djtext = analyzed

    if(charcount == "on"):
        analyzed = len(djtext)

        shree = {'purpose': 'Total Number of Char', 'after_operation': analyzed}
        djtext = analyzed
        #return render(request, 'punc.html', shree)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r" :
                analyzed = analyzed + char

        shree = {'purpose': 'After New Line Remover', 'after_operation': analyzed}

    if(newlineremover != "on" and charcount != "on" and uppercase != "on" and  removepunch != "on" ):
        return HttpResponse("You Are Not Selecting Any OF The Option")

    return render(request, 'punc.html', shree)
