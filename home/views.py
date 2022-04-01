from os import remove
from string import punctuation
from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "Special.html")

def about(request):
    return render(request, "about.html")


def analyse(request):

    mytext = request.GET.get('text', 'default')
    rmvpunc = request.GET.get('removepunc', 'off')
    myupper = request.GET.get('uppercase', 'off')
    mynewline = request.GET.get('newline', 'off')
    myextraspace = request.GET.get('extraspace', 'off')
    mycharcount = request.GET.get('chrcounter', 'off')

    if rmvpunc == 'on':
        removedpunc = ""
        punctuation = '/?,.;-%\!$^"''"([]@#<{}>)'
        for chr in mytext:
            if not chr in punctuation:
                removedpunc += chr
        parms = {'Purpose': "Remove Punctation", "analysed_text": removedpunc}
        return render(request, 'analyse.html', parms)

    elif myupper == 'on':
        uppercase = ''
        for chr in mytext:
            uppercase += chr.upper()
        parms = {'Purpose': "Text UPPERCASE", "analysed_text": uppercase}
        return render(request, 'analyse.html', parms)

    elif mynewline == 'on':
        newLine = ''
        for chr in mytext:
            if chr != '\n':
                newLine += chr
        parms = {'Purpose': "NewLine Removed", "analysed_text": newLine}
        return render(request, 'analyse.html', parms)

    elif myextraspace == "on":
        extraspace = ''
        for index, chr in enumerate(mytext):
            if not(mytext[index] == ' ' and mytext[index+1] == ' '):
                extraspace += chr
        parms = {'Purpose': "Extra Space Removed", "analysed_text": extraspace}
        return render(request, 'analyse.html', parms)

    elif mycharcount == "on":
        chrcount = ''
        for index, chr in enumerate(mytext):
            if not(mytext[index] == ' '):
                chrcount += chr

        parms = {'Purpose': "Chracter Count", "analysed_text": len(chrcount)}
        return render(request, 'analyse.html', parms)

    else:
        parms = {'Purpose': "Not Selected", "analysed_text": '-----'}
        return render(request, 'analyse.html', parms)
