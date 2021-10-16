from django.shortcuts import render
from django.http.response import HttpResponse



def home(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps= request.GET.get('fullcaps','off')
    nlr= request.GET.get('nlr','off')
    esr= request.GET.get('esr','off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char  not in punctuations:
                analyzed = analyzed + char
        params ={'purpose':'Removepunc','analyze_text':analyzed}
        return render(request,'analyze.html',params)
    
    
    elif(fullcaps=="on"):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params ={'purpose':'Change To Uppercase','analyze_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(nlr=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params ={'purpose':'New Line Remover','analyze_text':analyzed}
        return render(request,'analyze.html',params) 
    
    
    elif(esr=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index +1] ==" ":
                pass
            else:
                analyzed = analyzed + char
        params ={'purpose':'Extra Space Remover','analyze_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        print("error")