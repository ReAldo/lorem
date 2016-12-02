from rest_framework import serializers
from models import *


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ['pk', 'text']
