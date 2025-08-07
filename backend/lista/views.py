from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fiels = ['comprado']
