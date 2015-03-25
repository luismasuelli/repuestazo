from django.conf.urls import patterns, url
from .api import CheapestReplacementsListAPI

urlpatterns = patterns('',
    url(r'^cheap$', CheapestReplacementsListAPI.as_view(), name='cheap-replacements'),
)
