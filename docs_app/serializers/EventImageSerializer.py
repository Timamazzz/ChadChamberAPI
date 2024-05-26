from drf_writable_nested import WritableNestedModelSerializer

from docs_app.models import EventImage
from rest_framework import serializers


class EventImageSerializer(WritableNestedModelSerializer):
    file = serializers.CharField()

    class Meta:
        model = EventImage
        exclude = ('event',)
