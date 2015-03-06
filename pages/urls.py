from django.conf.urls import patterns, url
from pages.views import TemplateViewWithContext

urlpatterns = patterns('',
    url(r'^$', TemplateViewWithContext.as_view(template_name='pages/coming-soon.html'), name='index'),
)
