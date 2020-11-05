from django.http import HttpResponse
from django.shortcuts import render
import operator
from datetime import date


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def wordcount(request):
    return render(request, 'wordcount.html')


def friday(request):
    return render(request, 'friday.html')


def poisonedwine(request):
    return render(request, 'poisonedwine.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})


def fridayfound(request):
    year = int(request.GET['year'])
    if year <= 0:
        return render(request, 'friday.html')
    countf = 0
    word = ""
    for months in range(1, 13):
        if date(year, months, 13).weekday() == 4:
            countf += 1
    if countf == 1:
        word = "is " + str(countf)
    else:
        word = "are " + str(countf)

    return render(request, 'fridayfound.html', {'year': year, 'word': word})


def poison(request):
    r = list(request.GET['r'])
    for i in range(0, len(r)):
        r[i] = int(r[i])
    number = sum(2**i for i in r)

    return render(request, 'poisonedwinefound.html', {'number': number})
