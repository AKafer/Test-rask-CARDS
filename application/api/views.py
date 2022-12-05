from cards.models import Card, Transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

# from .filters import TagOperatorFilter
from .serializers import CardSerializer, TransactionSerializer


class CardViewSet(viewsets.ModelViewSet):
    """Класс представления карт"""
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """Класс представления карт"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('card', )
