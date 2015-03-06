from rest_framework.serializers import ModelSerializer
from customers.models import Contact


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'city', 'phone_number', 'address', 'content')