from django.conf.urls import patterns, url
import api

urlpatterns = patterns('',
    url(r'^contact$', api.ContactSendAPIView.as_view(), name='contact-send'),
)