from rest_framework.serializers import ModelSerializer
from .models import Banner, Reel, ReelImage, TextSet, TextSetElement


class BannerSerializer(ModelSerializer):

    class Meta:
        model = Banner
        exclude = ('created_on', 'updated_on', 'banner_type', 'code')


class ReelSerializer(ModelSerializer):

    class InlineReelImageSerializer(ModelSerializer):

        class Meta:
            model = ReelImage
            exclude = ('sequence', 'name', 'description', 'image', 'height', 'width', 'target')

    image_list = InlineReelImageSerializer()

    class Meta:
        model = Reel
        exclude = ('created_on', 'updated_on', 'reel_type', 'code')


class TextSetSerializer(ModelSerializer):

    class TextSetElementSerializer(ModelSerializer):

        class Meta:
            model = TextSetElement
            fields = ('code', 'value')

    entries = TextSetElementSerializer()

    class Meta:
        model = TextSet
        exclude = ('created_on', 'updated_on', 'text_set_type', 'code')