from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from docs_app.serializers.EventImageSerializer import EventImageSerializer
from feed_app.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    event_type = serializers.CharField(source='event_type.name')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Event
        fields = ('id', 'event_type', 'category', 'start_datetime', 'end_datetime', 'title')


class EventRetrieveSerializer(WritableNestedModelSerializer):
    images = EventImageSerializer()

    class Meta:
        model = Event
        fields = ('id', 'event_type', 'category', 'start_datetime', 'end_datetime', 'address', 'images', 'text')
