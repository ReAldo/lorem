from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('generator.urls', namespace='generator')),
    url(r'^phrases/', include('phrases.urls', namespace='phrases')),
    url(r'^saves/', include('saves.urls', namespace='saves')),
]
