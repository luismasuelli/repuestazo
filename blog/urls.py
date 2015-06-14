from django.conf.urls import patterns, url
from blog import api as blog_api

urlpatterns = [
    url('^summary$', blog_api.ListEntriesMonths.as_view(), name='blog-summary'),
    url('^entries/(?P<year>\d+)/(?P<month>\d+)$', blog_api.ListEntries.as_view(), name='blog-month'),
    url('^entry/(?P<pk>\d+)$', blog_api.GetEntry.as_view(), name='blog-entry')
]