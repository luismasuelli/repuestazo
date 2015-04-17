from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from grimoire.django.xmail.admin import AsyncEmailEntry, AsyncMailAdmin
from .admin import site

site.register(AsyncEmailEntry, AsyncMailAdmin)

urlpatterns = patterns('',
    url(r'', include('pages.urls')),
    url(r'^customers/', include('customers.urls')),
    url(r'^ads/', include('advertisement.urls')),
    url(r'^replacements/', include('stock.urls')),
    url(r'^admin/', include(site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
