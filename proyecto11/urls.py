from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyecto11.apps.usuario.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto11.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', principal),
)