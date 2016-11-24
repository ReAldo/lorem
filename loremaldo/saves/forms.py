from django import forms
from models import *


class SaveForm(forms.ModelForm):
    class Meta:
        model = Save
        fields = ['text']
