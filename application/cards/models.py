from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Card(models.Model):
    """
    Класс карт.
    """
    CHOICES = (
        ('not_activated', 'not_activated'),
        ('active', 'active'),
        ('expired', 'expired'),
    )

    series = models.IntegerField(
        validators=[
            MaxValueValidator(9999),
            MinValueValidator(1000)
        ])

    number = models.IntegerField(
        validators=[
            MaxValueValidator(999999999999),
            MinValueValidator(100000000000)
        ])
    date_issue = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField()
    limit = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=30,
        choices=CHOICES,
        default='created')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.series} - {self.number}'


class Transaction(models.Model):
    """
    Класс карт.
    """
    CHOICES = (
        ('purchase', 'purchase'),
        ('adding', 'adding'),
        ('transfer', 'transfer'),
    )
    sum = models.IntegerField()
    date = models.DateField()
    type = models.CharField(max_length=30, choices=CHOICES)
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE, related_name='card'
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str({self.id})
