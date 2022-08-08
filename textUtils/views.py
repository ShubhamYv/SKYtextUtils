# I'VE CREATED THIS FILE- SHUBHAM

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djText= request.POST.get('text', 'default')

    # check checkbox values
    removePunc= request.POST.get('removePunc', 'off')
    fullCaps= request.POST.get('fullCaps', 'off')
    newLineRemover= request.POST.get('newLineRemover', 'off')
    extraSpaceRemover= request.POST.get('extraSpaceRemover', 'off')

    # check which checkbox is ON
    if removePunc== "on":
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punctuations:
                analyzed= analyzed+ char
        dict= {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djText= analyzed

    if fullCaps== "on":
        analyzed= ""
        for char in djText:
            analyzed= analyzed + char.upper()
        dict = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        djText= analyzed

    if newLineRemover== "on":
        analyzed = ""
        for char in djText:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        dict = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djText= analyzed

    if extraSpaceRemover== "on":
        analyzed = ""
        for index,char in enumerate(djText):
            if not(djText[index] == " " and djText[index+1] == " "):
                analyzed = analyzed + char
        dict = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', dict)

    if removePunc!= "on" and fullCaps!= "on" and newLineRemover != "on" and extraSpaceRemover != "on":
        return HttpResponse("Please Select Any Operation and Try Again!")

    return render(request, 'analyze.html', dict)
