from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Replacement
from .serializers import ReplacementListSerializer, ReplacementRetrieveSerializer


class CheapestReplacementsListAPI(ListAPIView):
    serializer_class = ReplacementListSerializer
    queryset = Replacement.objects.cheapest()


class CheapestReplacementsRetrieveAPI(RetrieveAPIView):
    serializer_class = ReplacementRetrieveSerializer
    queryset = Replacement.objects.all()