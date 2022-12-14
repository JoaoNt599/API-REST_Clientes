from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ClientesViewSet(viewsets.ModelViewSet):
    """
    Listando clientes
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    """
    Adicinonando Ordernação
    """
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    """
    Exibindo clientes ativos e não ativos
    """
    filterset_fields = ['ativo']
    """
    Autenticando usuarios
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]