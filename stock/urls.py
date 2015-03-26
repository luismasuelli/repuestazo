from django.conf.urls import patterns, url
from .api import CheapestReplacementsListAPI, CheapestReplacementsRetrieveAPI

urlpatterns = patterns('',
    url(r'^cheap$', CheapestReplacementsListAPI.as_view(), name='cheap-replacement-list'),
    url(r'^cheap/(?P<pk>\d+)$', CheapestReplacementsRetrieveAPI.as_view(lookup_field='pk'), name='cheap-replacement-retrieve')
)
