from django.db import models

# Create your models here.
class ConnectionsGame(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    num_categories = models.IntegerField()
    words_per_category = models.IntegerField()

    def __str__(self):
        return self.title

class Category(models.Model):
    related_game = models.ForeignKey(
        'connections_app.ConnectionsGame',
        related_name='categories',
        on_delete=models.CASCADE
    )  # Link to ConnectionsGame
    category = models.CharField(max_length=200)
    difficulty = models.IntegerField()

    def __str__(self):
        return self.category

class Word(models.Model):
    category = models.ForeignKey(
        'connections_app.Category',
        related_name='words',
        on_delete=models.CASCADE
    )
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word