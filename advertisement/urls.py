from django.conf.urls import patterns, url
from .api import BannerView, ReelView, TextSetView, RandomTextSetView, RandomBannerView

urlpatterns = patterns('',
    url(r'^reel/(?P<pk>\d+)$', ReelView.as_view(), name='retrieve-reel'),
    url(r'^banner/(?P<pk>\d+)$', BannerView.as_view(), name='retrieve-banner'),
    url(r'^text-set/(?P<pk>\d+)$', TextSetView.as_view(), name='retrieve-text-set'),
    url(r'^random-reel/(?P<pk>\d+)$', RandomBannerView.as_view(), name='retrieve-random-reel'),
    url(r'^random-banner/(?P<pk>\d+)$', RandomTextSetView.as_view(), name='retrieve-random-banner')
)
