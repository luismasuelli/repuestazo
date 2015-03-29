from rest_framework.serializers import ModelSerializer
from .models import Banner, Reel, ReelImage, TextSet, TextSetElement, TextSetTypeField, RandomBanner, RandomTextSet


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

        class TextSetElementFieldSerializer(ModelSerializer):

            class Meta:
                model = TextSetTypeField
                fields = ('code',)

        field = TextSetElementFieldSerializer()

        class Meta:
            model = TextSetElement
            fields = ('field', 'value')

    entries = TextSetElementSerializer()

    class Meta:
        model = TextSet
        exclude = ('created_on', 'updated_on', 'text_set_type', 'code')


class RandomBannerSerializer(ModelSerializer):

    random = BannerSerializer()

    class Meta:
        model = RandomBanner
        fields = ('name', 'description', 'random')


class RandomTextSetSerializer(ModelSerializer):

    random = TextSetSerializer()

    class Meta:
        model = RandomTextSet
        fields = ('name', 'description', 'random')