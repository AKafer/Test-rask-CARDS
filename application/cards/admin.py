from django.contrib import admin

from .models import Card, Transaction


class CardAdmin(admin.ModelAdmin):
    """Класс отображения в админке задач"""
    list_display = (
        'id', 'series', 'number',
        'date_issue', 'date_expiration',
        'limit', 'status')
    list_display_links = (
        'id', 'series', 'number',
        'date_issue', 'date_expiration',
        'limit', 'status'
    )
    search_fields = (
        'series', 'number',
        'date_issue', 'date_expiration',
        'limit', 'status'
    )
    list_filter = ('series', 'number',
                   'date_issue', 'date_expiration',
                   'status')
    empty_value_display = '-пусто-'


class TransactionAdmin(admin.ModelAdmin):
    """Класс отображения в админке задач"""
    list_display = ('id', 'sum', 'date', 'type', 'card')
    list_display_links = ('id', 'sum', 'date', 'type', 'card')
    search_fields = ('sum', 'date', 'type', 'card')
    list_filter = ('sum', 'date', 'type', 'card')
    empty_value_display = '-пусто-'


admin.site.register(Card, CardAdmin)
admin.site.register(Transaction, TransactionAdmin)
