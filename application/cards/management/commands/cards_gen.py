
from datetime import datetime, timedelta
from random import randint

import pytz
from cards.models import Card
from django.core.management import BaseCommand

utc = pytz.UTC


SERIES = 4567
NUMBER_CARDS = 5
ACTIVE_PERIOD = 180


class Command(BaseCommand):

    def create_cards(self, numbers):
        new_cards = [
            Card(
                series=SERIES,
                number=number,
                date_expiration=(
                    (datetime.now() +
                     timedelta(days=ACTIVE_PERIOD))
                    .replace(tzinfo=utc)
                ),
                limit=(number % 1000) * randint(1, 10),
                status='active' if number < 500000000000 else 'not_activated'
            )
            for number in numbers
        ]
        Card.objects.bulk_create(new_cards)
        print('Новые карты успешно созданы')

    def handle(self, *args, **kwargs):
        numbers = []
        for i in range(NUMBER_CARDS):
            while True:
                number = randint(100000000000, 999999999999)
                if (
                    not Card.objects.filter(
                        number=number, series=SERIES
                        ).exists()
                        and number not in numbers):
                    numbers.append(number)
                    break
        self.create_cards(numbers)
