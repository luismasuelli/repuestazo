from rest_framework.generics import ListAPIView
from .models import Replacement
from .serializers import ReplacementSerializer


class CheapestReplacementsListAPI(ListAPIView):
    serializer_class = ReplacementSerializer
    queryset = Replacement.objects.cheapest()