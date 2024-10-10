from django.db import models
from users.models import User

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    user_sender = models.ForeignKey(User, related_name='sent_movies', on_delete=models.CASCADE)
    user_receiver = models.ForeignKey(User, related_name='received_movies', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} (from {self.user_sender.username} to {self.user_receiver.username})"
