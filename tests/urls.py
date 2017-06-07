from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()


def tester(request):
    return HttpResponse("Hello")


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^password/$', include('simple_auth.urls')),
    url(r'^tester/hello/$', view=tester),
    url(r'^goodbye/world/$', view=tester),
    url(r'^$', view=tester),
]
