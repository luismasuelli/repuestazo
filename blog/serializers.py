from .models import Entry, MonthEntriesBreakdown
from rest_framework.serializers import ModelSerializer


class EntrySerializer(ModelSerializer):

    class Meta:
        model = Entry
        fields = ('created_on', 'title', 'slug', 'category', 'content')


class EntryPreviewSerializer(ModelSerializer):

    class Meta:
        model = Entry
        fields = ('created_on', 'title', 'slug', 'category', 'preview')


class MonthEntriesBreakdownSerializer(ModelSerializer):

    class Meta:
        model = MonthEntriesBreakdown
        fields = ('created_year', 'created_month', 'entries_count')