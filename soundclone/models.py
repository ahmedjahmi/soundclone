from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    # the following line is probably redudndant now that we're adding artist profile
    artist_name = models.CharField(max_length=225)
    duration = models.IntegerField()
    artwork = models.ImageField(
        upload_to='images',
        height_field=None,
        width_field=None,
        max_length=100
    )
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    # shares

    def is_liked_by(self, user):
        return self.like_set.filter(user=user).exists()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    body = models.TextField()


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    tracks = models.ManyToManyField(Track)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# User
# Playlist
# Artwork
# Like
# Share
# Follow