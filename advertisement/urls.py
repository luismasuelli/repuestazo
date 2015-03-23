from django.conf.urls import patterns, url
from .api import BannerView, ReelView

urlpatterns = patterns('',
    url(r'^reel/(?P<pk>\d+)$', ReelView.as_view(), name='retrieve-reel'),
    url(r'^banner/(?P<pk>\d+)$', BannerView.as_view(), name='retrieve-banner'),
)
