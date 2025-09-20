from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['comprado']

    def get_queryset(self):
        if self.action == 'list':
            return Item.objects.filter(comprado=False)

        return Item.objects.all()
    

    @action(detail=False, methods=['get'])
    def historico(self, request):
        itens_comprados = Item.objects.filter(comprado=True).order_by('-atualizado_em')
        