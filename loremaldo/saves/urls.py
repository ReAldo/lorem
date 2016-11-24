from django.conf.urls import url
import views

urlpatterns = [
    url(
        r'detail/(?P<pk>\d+)/',
        views.SaveDetailView.as_view(),
        name='save_detail'
    ),

    url(
        r'create/',
        views.SaveCreateView.as_view(),
        name='save_create'
    ),
]
