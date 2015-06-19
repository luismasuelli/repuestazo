# coding=utf-8
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import Entry, MonthEntriesBreakdown
from .serializers import EntryPreviewSerializer, EntrySerializer, MonthEntriesBreakdownSerializer


class ListEntriesMonths(ListAPIView):
    """
    obtiene una lista de año/mes/#entradas.
    """

    serializer_class = MonthEntriesBreakdownSerializer

    def get_queryset(self):
        """
        Los queryset en raw hay que generarlos en cada vuelta. Por esto es que
          uso get_queryset en lugar de poner algo en la propiedad queryset: los
          queryset raw no tienen método .all()
        """
        return MonthEntriesBreakdown.objects.do()


class GetEntry(RetrieveAPIView):
    """
    Obtiene una entrada, en modo normal, por id.
    """

    serializer_class = EntrySerializer
    queryset = Entry.objects.all().full()


class ListEntries(ListAPIView):
    """
    Para un /año/mes obtiene todas las entradas pero en modo preview.
    """

    serializer_class = EntryPreviewSerializer
    queryset = Entry.objects.preview()

    def get_queryset(self):
        return super(ListEntries, self).get_queryset().for_month(self.kwargs['year'], self.kwargs['month']).order_by('-created_on')
