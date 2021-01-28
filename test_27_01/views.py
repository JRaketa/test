from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    fulltextFlat = fulltext.split()
    wordsLib = {}
    wordsLibPar = {'wordsCount': len(fulltextFlat),
                    'fulltext' : fulltext}

    for word in fulltextFlat:
        if word in wordsLib:
            wordsLib[word] += 1
        else:
             wordsLib[word] = 1

    wordsLibArangedList =  wordsLib.items()
    wordslibaranged = sorted(wordsLibArangedList,
                             key = operator.itemgetter(1), reverse = True)

    wordsLibPar['wordslibaranged'] = wordslibaranged
    

    return render(request, 'count.html',
                  wordsLibPar)

def about(request):
    return render(request, 'about.html')
