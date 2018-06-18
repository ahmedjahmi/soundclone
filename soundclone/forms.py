from django.forms import ModelForm

from .models import Track
from .models import Comment

class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'file', 'artist_name', 'artwork']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]