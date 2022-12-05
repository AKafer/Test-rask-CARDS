from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CardViewSet, TransactionViewSet

router = DefaultRouter()

router.register(r'cards', CardViewSet, basename='cards')
router.register(r'transactions', TransactionViewSet, basename='transactions')

urlpatterns = [
    path('', include(router.urls)),
]
