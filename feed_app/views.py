from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ChadChamberAPI.utils.ModelViewSet import ModelViewSet
from feed_app.models import Event
from feed_app.serializers.EventSerializer import EventSerializer, EventRetrieveSerializer, EventListSerializer


# Create your views here.
class EventViewSet(ModelViewSet):
    queryset = Event.objects.filter(is_published=True).order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EventSerializer
    serializer_list = {
        'retrieve': EventRetrieveSerializer,
        'list': EventListSerializer,
    }


