from docs_app.models import EventImage
from rest_framework import serializers


class EventImageSerializer(serializers.ModelSerializer):
    file = serializers.CharField()

    class Meta:
        model = EventImage
        exclude = ('event',)
