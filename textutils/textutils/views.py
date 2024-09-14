# i have created this file 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):       
    return render(request, 'index.html')    

def analyze(request):
    # get the text
    # get the text
    djtext = request.POST.get('text', 'default')
   
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')   
    newlineremover = request.POST.get('newlineremover', 'off')   
    extraspaceremover = request.POST.get('extraspaceremover', 'off')  
    charcount = request.POST.get('charcount', 'off')    

    if removepunc == "on":

        punctuation = '''[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]'''
        analyzed_txt = ""
        for char in djtext:
            if char not in punctuation:
                analyzed_txt = analyzed_txt + char
        params= {
        'purpose':'Remove Punctuation ',
        'analyzed_text': analyzed_txt
        }
        djtext = analyzed_txt

    if fullcaps == "on":
        analyzed_txt = ""
        for char in djtext:
            analyzed_txt = analyzed_txt + char.upper()
        
        params = {
            'purpose':'Changed to Uppercase',
            'analyzed_text': analyzed_txt
        }
        djtext = analyzed_txt

    if newlineremover == "on":
        analyzed_txt = ""
        for char in djtext:
            if char !='\n':
                analyzed_txt = analyzed_txt + char
        
        params={
            'purpose':'New Line Remover',
            'analyzed_text': analyzed_txt
        }
        djtext = analyzed_txt 

    if extraspaceremover == "on":
        analyzed_txt = ""
        for index, char in enumerate(djtext):
            if index < len(djtext) - 1:
                if not(djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed_txt = analyzed_txt + char
                else:
                    analyzed_txt = analyzed_txt + char
            else:
                analyzed_txt = analyzed_txt + char        
        
        params = {
            'purpose':'New Line Remover',
            'analyzed_text': analyzed_txt
        }
        djtext = analyzed_txt

    if charcount == "on":
        charcount = 0
        for index, char in enumerate(djtext):
            charcount += 1
        
        params = {
            'purpose':'',
            'analyzed_text': analyzed_txt,
            'charcount':charcount
        }

    if(removepunc!="on" and fullcaps!="on" and extraspaceremover!="on" and newlineremover !="on" and charcount!="on"):
            params = {
            'purpose':'Error ... ',
            'analyzed_text': "No option selected. Please select an option to perform the text utilities operation."
        }          
      
    return render(request, 'analyze.html', params)    


def capfirst(request):
    return HttpResponse("This is capitalizefirst page")

def newlineremove(request):
    return HttpResponse("This is newlineremove page")

def spaceremove(request):
    return HttpResponse("This is spaceremove page")

def charcount(request):
    return HttpResponse("This is charcount page")




