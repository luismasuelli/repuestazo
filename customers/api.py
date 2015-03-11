from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.generics import CreateAPIView
from .serializers import ContactSerializer


class ContactSendAPIView(CreateAPIView):

    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        result = super(ContactSendAPIView, self).post(request, *args, **kwargs)
        try:
            send_mail(subject="Nueva consulta",
                      message=render_to_string('customers/mail.contact.txt', request.DATA),
                      from_email=settings.DEFAULT_FROM_EMAIL,
                      recipient_list=settings.DEFAULT_RECIPIENTS['contact'],
                      fail_silently=True,
                      html_message=render_to_string('customers/mail.contact.html', request.DATA))
        except Exception as e:
            pass
        return result