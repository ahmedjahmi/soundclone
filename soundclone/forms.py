from django.forms import ModelForm

from .models import Track
from .models import Comment
from .models import Playlist


class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'file', 'artist_name', 'artwork']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['name']
