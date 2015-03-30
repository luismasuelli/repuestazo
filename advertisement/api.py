from rest_framework.generics import RetrieveAPIView
from .serializers import ReelSerializer, BannerSerializer, RandomBannerSerializer, RandomTextSetSerializer, \
    TextSetSerializer
from .models import Reel, TextSet, Banner, RandomBanner, RandomTextSet


class BannerView(RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class ReelView(RetrieveAPIView):
    queryset = Reel.objects.ready()
    serializer_class = ReelSerializer


class TextSetView(RetrieveAPIView):
    queryset = TextSet.objects.all()
    serializer_class = TextSetSerializer


class RandomBannerView(RetrieveAPIView):
    queryset = RandomBanner.objects.all()
    serializer_class = RandomBannerSerializer


class RandomTextSetView(RetrieveAPIView):
    queryset = RandomTextSet.objects.all()
    serializer_class = RandomTextSetSerializer