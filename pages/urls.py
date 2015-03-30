from django.conf.urls import patterns, url
from django.views.decorators.csrf import ensure_csrf_cookie
from pages.views import TemplateViewWithContext

urlpatterns = patterns('',
    # url(r'^$', ensure_csrf_cookie(TemplateViewWithContext.as_view(template_name='pages/coming-soon.html')), name='coming-soon'),
    url(r'^$', ensure_csrf_cookie(TemplateViewWithContext.as_view(template_name='pages/index.html')), name='index'),
)

