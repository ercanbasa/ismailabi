from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ismailabi.quotes.views.home', name='home'),
    url(r'^quote/(?P<id>\w+)/$', 'ismailabi.quotes.views.quote', name='quote'),
    url(r'^admin/', include(admin.site.urls)),
)
