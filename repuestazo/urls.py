from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'', include('pages.urls')),
    # url(r'^ads/', include('advertisement.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
