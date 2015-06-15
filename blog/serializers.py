from .models import Entry, MonthEntriesBreakdown, Category
from rest_framework.serializers import ModelSerializer, SlugRelatedField


class EntrySerializer(ModelSerializer):

    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Entry
        fields = ('created_on', 'title', 'slug', 'category', 'content')


class EntryPreviewSerializer(ModelSerializer):

    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Entry
        fields = ('created_on', 'title', 'slug', 'category', 'preview')


class MonthEntriesBreakdownSerializer(ModelSerializer):

    class Meta:
        model = MonthEntriesBreakdown
        fields = ('created_year', 'created_month', 'entries_count')