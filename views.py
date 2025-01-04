# I have created this file-- khemchand
from django.http import HttpResponse
from django.shortcuts import render

##code for video 6
# def index(request):
#     return HttpResponse('''<h1>khemchand sharma</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django Code With Harry</a>''')
# def about(request):
#     return HttpResponse('about khemu')


######## code for video 7#######


def index(request):
    # Return the home page
    params = {'name': 'khemu', 'place': 'kosi kalan'}
    return render(request, 'index.html', params)

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Initialize analyzed text
    analyzed = djtext

    # Apply transformations in sequence
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\?@#$%^&*_~`'''
        analyzed = "".join(char for char in analyzed if char not in punctuations)

    if fullcaps == "on":
        analyzed = analyzed.upper()

    if newlineremover == "on":
        analyzed = "".join(char for char in analyzed if char != "\n" and char != "\r")

    if extraspaceremover == "on":
        analyzed = " ".join(analyzed.split())

    char_count = None
    if charcount == "on":
        char_count = len(analyzed)

    # Prepare parameters for rendering
    params = {
        'purpose': 'Text Analysis',
        'analyzed_text': analyzed,
    }

    if char_count is not None:
        params['char_count'] = char_count

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and  extraspaceremover != "on" and charcount != "on":
        return HttpResponse("Error: No options were selected. Please select at least one option.")

    # Return the response
    return render(request, 'analyze.html', params)


