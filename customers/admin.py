from django.contrib.admin import ModelAdmin, site
from customers.models import Contact


class ContactAdmin(ModelAdmin):

    list_display = ['created_on', 'updated_on', 'name', 'email', 'city', 'phone_number']

    def has_add_permission(self, request):
        return False


site.register(Contact, ContactAdmin)