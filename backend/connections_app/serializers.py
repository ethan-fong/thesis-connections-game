from rest_framework import serializers
from .models import ConnectionsGame, Category, Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category', 'difficulty', 'words']

class ConnectionsGameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = ConnectionsGame
        fields = ['title', 'created_at', 'num_categories', 'words_per_category', 'categories']
