from rest_framework.generics import CreateAPIView
from .serializers import ContactSerializer


class ContactSendAPIView(CreateAPIView):

    serializer_class = ContactSerializer