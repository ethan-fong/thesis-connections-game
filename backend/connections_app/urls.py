from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConnectionsGameViewSet, CategoryViewSet, WordViewSet
from .views import ConnectionsGameDetailAPIView

router = DefaultRouter()
router.register(r'connectionsgames', ConnectionsGameViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'words', WordViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
    path('getgame/<int:pk>/', ConnectionsGameDetailAPIView.as_view(), name='get-game'),
]