from rest_framework.serializers import ModelSerializer
from .models import Replacement


class ReplacementListSerializer(ModelSerializer):

    class Meta:
        model = Replacement
        fields = ('id', 'product', 'brand', 'model', 'year', 'discount')


class ReplacementRetrieveSerializer(ModelSerializer):

    class Meta:
        model = Replacement
        fields = ('product', 'brand', 'model', 'year', 'discount', 'category', 'offer')