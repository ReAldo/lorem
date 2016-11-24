from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.views import generic
from models import *
from forms import *


class SaveDetailView(generic.DetailView):
    model = Save

    def get_context_data(self, **kwargs):
        context = super(SaveDetailView, self).get_context_data(**kwargs)
        context['site'] = get_current_site(self.request)
        return context


class SaveCreateView(generic.CreateView):
    model = Save
    form_class = SaveForm
