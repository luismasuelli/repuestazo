from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy as _


class RepuestazoAdminSite(AdminSite):
    site_header = _(u'Repuestazo.com administration')
    site_title = _(u'Repuestazo.com site admin')
site = RepuestazoAdminSite()