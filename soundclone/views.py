from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Track
from .forms import TrackForm


def track_list_view(request):
    tracks = Track.objects.all()
    return render(request, "templates/track_list.html", { 'tracks': tracks })

def track_create_view(request):
    if request.method == 'POST':
        # take data from form and save as new record
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            # TODO: save model form here instead
            cd = form.cleaned_data

            track = Track.objects.create(
                title=cd['title'],
                artist_name=cd['artist_name'],
                artwork=cd['artwork'],
                file=cd['file'],
                duration=200
            )
            return redirect('track-detail')
        else:
            return render(request, "templates/track_create.html", { 'form': form })
    else:
        form = TrackForm()
        return render(request, "templates/track_create.html", { 'form': form })

def track_detail_view(request, pk):
    track = Track.objects.get(pk=pk)
    return render(request, "templates/track_detail.html", { 'track': track })

def user_create_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user-detail', username=user.username)
        else:
            return render(request, "templates/user_create.html", { 'form': form })
    else:
        form = UserCreationForm()
        return render(request, "templates/user_create.html", { 'form': form })


def user_detail_view(request, username):
    user = User.objects.get(username=username)
    tracks = Track.objects.filter(artist=user)
    return render(request, "templates/user_detail.html", { 'user': user, 'tracks': tracks })