from django.http import HttpResponse
from django.shortcuts import render
"""def index(request):
    return HttpResponse("Home")"""
#def about(request):
#    return HttpResponse("about hello bhai");
#def page(request):
#   return HttpResponse("""<h1>nisarg</h1><br/><a href="http://www.google.com">google</a>""");
#def page1(request):
#   return HttpResponse("""<h1>nisarg1</h1><br/><a href="http://www.facebook.com">facebook</a>""");
def index(request):
    nis={'name':"nisarg",'salary':2000}
    return render(request, 'index.html',nis)
    # return HttpResponse("Home")

def removepunc(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    # here text is value of the name field of the input
    print(djtext)
    #Analyze the text
    return HttpResponse("remove punc")
def analyse(request):
    str1=""
    djtext = request.POST.get('text', 'default')
    print(djtext)
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    #print(removepunc)
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    print(newlineremover)
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # Check which checkbox is on
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        str1 =str1 + ','+"Removed Punctuations"
        params = {'purpose':str1, 'analyzed_text': analyzed}
        #return render(request, 'analyse.html', params)
        djtext=analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        str1 = str1 + ',' + "Changed to Uppercase"
        params = {'purpose': str1, 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyse.html', params)
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        str1 = str1 + ',' + "extra space remover"
        params = {'purpose':str1, 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        #return render(request, 'analyse.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        str1 = str1 + ',' + "Removed NewLines"
        # Analyze the text
        params = {'purpose': str1, 'analyzed_text': analyzed}
        djtext = analyzed
    print(analyzed)
    print(djtext)
    return render(request, 'analyse.html', params)


    # here text is value of the name field of the input
    # default is one type of alt field of img tag if the value of text name field is not found then
    # it print defult or off in our example
    # Analyze the text
    return HttpResponse("remove punc")
"""def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove first")


def spaceremove(request):
    return HttpResponse("space remover back")

def charcount(request):
    return HttpResponse("charcount ")"""
