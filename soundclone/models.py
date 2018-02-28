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

    # likes
    # shares





# User
# Playlist
# Artwork
# Like
# Share
# Follow