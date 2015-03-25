from rest_framework.serializers import ModelSerializer
from .models import Replacement


class ReplacementSerializer(ModelSerializer):

    class Meta:
        model = Replacement
        exclude = ('product', 'brand', 'model', 'year', 'discount')