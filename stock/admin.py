from django.contrib import messages
from django.contrib.admin import ModelAdmin, site
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from .models import Replacement
from .forms import UploadReplacementsForm


class ReplacementAdmin(ModelAdmin):

    change_list_template = 'stock/changelist.html'
    list_display = ('dealer', 'score', 'category', 'code', 'product', 'brand', 'model', 'year', 'stock', 'cost', 'price', 'offer', 'discount')
    list_display_links = ('product',)

    def get_urls(self):
        return patterns('',
            url(r'^upload/$', self.admin_site.admin_view(self.upload_replacements), name='stock_replacement_xlsupload')
        ) + super(ReplacementAdmin, self).get_urls()

    def upload_replacements(self, request):
        """
        Vista para cargar los repuestos.
        """
        form = UploadReplacementsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                Replacement.load_xls(form.cleaned_data['replacements'].file)
                self.message_user(request, _(u'The replacements file was successfully submitted'), level=messages.INFO)
            except Replacement.LoadError:
                self.message_user(request, _(u'An error occurred while loading the replacements file. Verify it is a valid XLSX file'), level=messages.ERROR)
        else:
            self.message_user(request, _(u'No replacements file was submitted'), level=messages.INFO)
        return redirect(to=reverse('admin:stock_replacement_changelist'))


site.register(Replacement, ReplacementAdmin)