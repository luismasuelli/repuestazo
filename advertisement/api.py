from rest_framework.generics import RetrieveAPIView
from .serializers import ReelSerializer, BannerSerializer
from .models import Reel


class BannerView(RetrieveAPIView):
    serializer_class = BannerSerializer


class ReelView(RetrieveAPIView):
    queryset = Reel.objects.ready()
    serializer_class = ReelSerializer
