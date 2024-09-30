from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    user_sender = models.ForeignKey(User, related_name='sent_movies', on_delete=models.CASCADE)
    user_receiver = models.ForeignKey(User, related_name='received_movies', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} (from {self.user_sender.username} to {self.user_receiver.username})"
