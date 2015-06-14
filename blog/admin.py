from django.contrib.admin import ModelAdmin
from repuestazo.admin import site
from .models import Category, Entry


class CategoryAdmin(ModelAdmin):
    pass


class EntryAdmin(ModelAdmin):

    exclude = ['preview']


site.register(Category, CategoryAdmin)
site.register(Entry, EntryAdmin)