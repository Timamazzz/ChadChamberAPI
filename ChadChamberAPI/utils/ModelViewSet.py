from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from ChadChamberAPI.utils.OptionsMetadata import OptionsMetadata


class ModelViewSet(viewsets.ModelViewSet):
    """
    A base class for representations of model sets.
    """
    serializer_list = {}  # Dictionary for storing serializers for each action
    metadata_class = OptionsMetadata  # Metadata class for views
    filter_backends = [DjangoFilterBackend, SearchFilter]

    def get_serializer(self, *args, **kwargs):
        """
        Getting the serializer.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
        """
        Getting the serializer class.
        """
        # Returning the serializer class for the current action or the default class
        return self.serializer_list.get(self.action, self.serializer_class)
