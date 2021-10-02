from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    Analyzed_Text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in Analyzed_Text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Successfully Removed  Punctuation Mark',
                  'analyzed_text': analyzed}
        Analyzed_Text = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in Analyzed_Text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Successfully Converted  To UPPERCASE',
                  'analyzed_text': analyzed}
        Analyzed_Text = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in Analyzed_Text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Successfully Removed New Line',
                  'analyzed_text': analyzed}
        Analyzed_Text = analyzed



    return render(request, 'analyze.html', params)
    

    

    
