from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ConnectionsGameViewSet, CategoryViewSet, WordViewSet
from .views import GetgameViewSet

router = DefaultRouter()
router.register(r'connectionsgames', ConnectionsGameViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'words', WordViewSet)
router.register(r'getgame', GetgameViewSet, basename='connectionsjson')


urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]