from django.shortcuts import render
from rest_framework import generics, status, viewsets
from .models import ConnectionsGame, Category, Word
from .serializers import ConnectionsGameSerializer, CategorySerializer, WordSerializer
from rest_framework.response import Response

class ConnectionsGameViewSet(viewsets.ModelViewSet):
    queryset = ConnectionsGame.objects.all()
    serializer_class = ConnectionsGameSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    
class ConnectionsGameDetailAPIView(generics.RetrieveAPIView):
    queryset = ConnectionsGame.objects.all()
    serializer_class = ConnectionsGameSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            game = ConnectionsGame.objects.get(pk=pk)
        except ConnectionsGame.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Get categories related to the ConnectionsGame
        categories = Category.objects.filter(related_game=game)
        category_serializer = CategorySerializer(categories, many=True)

        # Serialize the game data
        game_serializer = self.get_serializer(game)
        
        # Combine game data and categories
        data = game_serializer.data
        data['categories'] = category_serializer.data
        
        return Response(data)
    
class CategoryWordsAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = WordSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Get words related to the Category
        words = category.words.all()
        serializer = WordSerializer(words, many=True)
        
        return Response({'category': category.category, 'words': serializer.data})