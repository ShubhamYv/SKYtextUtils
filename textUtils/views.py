# I'VE CREATED THIS FILE- SHUBHAM

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djText= request.GET.get('text', 'default')

    # check checkbox values
    removePunc= request.GET.get('removePunc', 'off')
    fullCaps= request.GET.get('fullCaps', 'off')
    newLineRemover= request.GET.get('newLineRemover', 'off')
    extraSpaceRemover= request.GET.get('extraSpaceRemover', 'off')
    charCounter= request.GET.get('charCounter', 'off')


    # check which checkbox is ON
    if removePunc== "on":
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punctuations:
                analyzed= analyzed+ char
        dict= {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', dict)

    elif fullCaps== "on":
        analyzed= ""
        for char in djText:
            analyzed= analyzed + char.upper()
        dict = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', dict)

    elif newLineRemover== "on":
        analyzed = ""
        for char in djText:
            if char!= "\n":
                analyzed = analyzed + char
        dict = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', dict)

    elif extraSpaceRemover== "on":
        analyzed = ""
        for index, char in enumerate(djText):
            if not(djText[index]==" " and djText[index+1]==" "):
                analyzed = analyzed + char
        dict = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', dict)


    elif charCounter== "on":
        analyzed= ('Number of character is', len(djText))
        dict = {'purpose': 'Count the Characters', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', dict)



    else:
        return HttpResponse("Error")