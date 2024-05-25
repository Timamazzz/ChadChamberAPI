from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ChadChamberAPI.utils.ModelViewSet import ModelViewSet
from services_app.models import Service
from services_app.serializers.ServiceSerializer import ServiceSerializer, ServiceRetrieveSerializer, \
    ServiceListSerializer


# Create your views here.
class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ServiceSerializer
    serializer_list = {
        'retrieve': ServiceRetrieveSerializer,
        'list': ServiceListSerializer,
    }


