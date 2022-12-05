import pytz
from cards.models import Card, Transaction
from rest_framework import serializers

utc = pytz.UTC


class CardSerializer(serializers.ModelSerializer):
    """Класс сериализатора карт."""

    class Meta:
        fields = '__all__'
        model = Card


class TransactionSerializer(serializers.ModelSerializer):
    """Класс сериализатора карт."""

    class Meta:
        fields = '__all__'
        model = Transaction
