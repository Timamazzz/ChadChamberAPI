from rest_framework import serializers

from services_app.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'short_description')


class ServiceRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('name', 'text')
