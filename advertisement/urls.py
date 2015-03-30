from django.conf.urls import patterns, url
from .api import BannerView, ReelView, TextSetView, RandomTextSetView, RandomBannerView

urlpatterns = patterns('',
    url(r'^reel/(?P<code>[a-zA-Z0-9_-]+)$', ReelView.as_view(lookup_field='code'), name='retrieve-reel'),
    url(r'^banner/(?P<code>[a-zA-Z0-9_-]+)$', BannerView.as_view(lookup_field='code'), name='retrieve-banner'),
    url(r'^text-set/(?P<code>[a-zA-Z0-9_-]+)$', TextSetView.as_view(lookup_field='code'), name='retrieve-text-set'),
    url(r'^random-banner/(?P<code>[a-zA-Z0-9_-]+)$', RandomBannerView.as_view(lookup_field='code'), name='retrieve-random-reel'),
    url(r'^random-text-set/(?P<code>[a-zA-Z0-9_-]+)$', RandomTextSetView.as_view(lookup_field='code'), name='retrieve-random-banner')
)
