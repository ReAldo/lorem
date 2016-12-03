from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.PhraseList.as_view(), name='phrase_list'),
    url(r'^create/$', views.PhraseCreate.as_view(), name='phrase_create'),

    url(r'^lorem/$', views.RandomLorem.as_view(), name='lorem'),
    url(r'^lorem/(?P<n>\d+)/$', views.RandomLorem.as_view(), name='lorem'),
]
