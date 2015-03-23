from rest_framework.serializers import ModelSerializer
from .models import Banner, Reel, ReelImage


class BannerSerializer(ModelSerializer):

    class Meta:
        model = Banner
        exclude = ('created_on', 'updated_on', 'banner_type', 'code')


class ReelSerializer(ModelSerializer):

    class InlineReelImageSerializer(ModelSerializer):

        class Meta:
            model = ReelImage
            exclude = ('reel', 'created_on', 'updated_on')

    image_list = InlineReelImageSerializer()

    class Meta:
        model = Reel
        exclude = ('created_on', 'updated_on', 'reel_type', 'code')