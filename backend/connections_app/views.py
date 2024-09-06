from time import sleep

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import ConnectionsGame, Category, Word
from .serializers import ConnectionsGameSerializer, CategorySerializer, WordSerializer

class ConnectionsGameViewSet(viewsets.ModelViewSet):
    queryset = ConnectionsGame.objects.all()
    serializer_class = ConnectionsGameSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class GetgameViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        print("sleeping to simulate server load")
        sleep(3)
        if pk is None:
            # Handle the case where no `pk` is provided
            return Response({"error": "Game ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            game = ConnectionsGame.objects.get(pk=pk)
        except ConnectionsGame.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)
        # Serialize the game data
        serializer = ConnectionsGameSerializer(game)
        return Response(serializer.data)
