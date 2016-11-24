from django.shortcuts import render
from phrases.models import Phrase
from random import sample


def generate(request):
    phrases = Phrase.objects.all()

    phrases = sample(phrases, 5)

    return render(request, 'generator/generate.html', {
        'phrases': phrases
    })
