from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from grimoire.django.xmail.admin import AsyncEmailEntry, AsyncMailAdmin
from grimoire.django.dynsettings.admin import DynamicSetting, DynamicSettingAdmin
from .admin import site

site.register(AsyncEmailEntry, AsyncMailAdmin)
site.register(DynamicSetting, DynamicSettingAdmin)

urlpatterns = patterns('',
    url(r'', include('pages.urls')),
    url(r'^customers/', include('customers.urls')),
    url(r'^ads/', include('advertisement.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^replacements/', include('stock.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
