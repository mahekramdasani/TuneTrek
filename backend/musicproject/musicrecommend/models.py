# musicrecommend/models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from api.models import CustomUser 

# from api.models import UserLike  # Import the UserLike model from the 'api' app

class Song(models.Model):
    song_id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    lyrics = models.TextField()
    image_url = models.URLField()
    # likes = models.ManyToManyField(CustomUser, through=UserLike, related_name='song_likes')

    def __str__(self):
        return self.title
