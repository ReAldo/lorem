from rest_framework import generics
from serializers import *
from rest_framework import views
import random


class RandomLorem(views.APIView):
    def get(self, request, n=5):
        rng = xrange(0, Phrase.objects.count())
        choices = random.sample(rng, int(n))

        phrases = []
        for i in choices:
            phrases.append(Phrase.objects.all()[i])

        return views.Response(PhraseSerializer(phrases, many=True).data)


class PhraseList(generics.ListAPIView):
    serializer_class = PhraseSerializer
    queryset = Phrase.objects.all()


class PhraseCreate(generics.CreateAPIView):
    serializer_class = PhraseSerializer
