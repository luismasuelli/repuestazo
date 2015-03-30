from rest_framework.serializers import ModelSerializer
from .models import Banner, Reel, ReelImage, TextSet, TextSetElement, TextSetTypeField, RandomBanner, RandomTextSet


class BannerSerializer(ModelSerializer):

    class Meta:
        model = Banner
        exclude = ('created_on', 'updated_on', 'banner_type', 'id')


class ReelSerializer(ModelSerializer):

    class InlineReelImageSerializer(ModelSerializer):

        class Meta:
            model = ReelImage
            fields = ('name', 'description', 'image')

    image_list = InlineReelImageSerializer(many=True)

    class Meta:
        model = Reel
        exclude = ('created_on', 'updated_on', 'reel_type', 'id')


class TextSetSerializer(ModelSerializer):

    class TextSetElementSerializer(ModelSerializer):

        class TextSetElementFieldSerializer(ModelSerializer):

            class Meta:
                model = TextSetTypeField
                fields = ('code',)

        text_field = TextSetElementFieldSerializer()

        class Meta:
            model = TextSetElement
            fields = ('text_field', 'value')

    entries = TextSetElementSerializer(many=True)

    class Meta:
        model = TextSet
        exclude = ('created_on', 'updated_on', 'text_set_type', 'id')


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