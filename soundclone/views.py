from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Track, Like, Comment, Playlist
from .forms import TrackForm, CommentForm, PlaylistForm


def track_list_view(request):
    tracks = Track.objects.all()
    return render(request, "templates/track_list.html", {'tracks': tracks})


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
                artist=request.user,
                artwork=cd['artwork'],
                file=cd['file'],
                duration=200
            )

            return redirect('track-detail', pk=track.pk)
        else:
            return render(
                request, "templates/track_create.html", {'form': form}
                )
    else:
        form = TrackForm()
        return render(request, "templates/track_create.html", {'form': form})


def track_detail_view(request, pk):
    track = Track.objects.get(pk=pk)
    # Comment.object.filter(track=track) is the same thing
    comments = track.comment_set.all()
    form = CommentForm()
    playlists = request.user.playlist_set.all()
    return render(
        request,
        "templates/track_detail.html",
        {'track': track, 'comments': comments, 'form': form, 'playlists': playlists }
    )


def track_like_view(request, pk):
    if request.user.is_authenticated:
        track = Track.objects.get(pk=pk)
        if track.is_liked_by(request.user):
            return redirect('track-detail', pk=track.pk)
        else:
            like = Like.objects.create(track=track, user=request.user)
            return redirect('track-detail', pk=track.pk)
    else:
        return redirect('login')


def track_unlike_view(request, pk):
    if request.user.is_authenticated:
        track = Track.objects.get(pk=pk)
        if track.is_liked_by(request.user):
            track.like_set.filter(user=request.user).delete()
            return redirect('track-detail', pk=track.pk)
        else:
            return redirect('track-detail', pk=track.pk)
    else:
        return redirect('login')
# TODO: add decorator for login authorization


def comment_create_view(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:

            # take data from form and save as new record
            track = Track.objects.get(pk=pk)
            form = CommentForm(request.POST)
            if form.is_valid():
                # TODO: save model form here instead
                cd = form.cleaned_data

                Comment.objects.create(
                    user=request.user,
                    track=track,
                    body=cd['body']
                )

                return redirect('track-detail', pk=track.pk)
            else:
                return render(
                    request,
                    "templates/track_detail.html",
                    {
                        'track': track,
                        'form': form,
                        'comments': track.comment_set.all()
                    }
                )
        else:
            return redirect('login')
    else:
        raise Http404("Invalid request, sorry!")


def comment_delete_view(request, pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=pk)
        track = comment.track

        comment.delete()
        return redirect('track-detail', pk=track.pk)
    else:
        return redirect('login')


def playlist_create_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:

            form = PlaylistForm(request.POST)
            if form.is_valid():

                cd = form.cleaned_data

                playlist = Playlist.objects.create(
                    name=cd['name'],
                    user=request.user
                )

                return redirect('playlist-detail', pk=playlist.pk)
            else:
                return render(
                    request, "templates/playlist_create.html", {'form': form}
                    )
        else:
            return redirect('login')
    else:
        form = PlaylistForm()
        return render(request, "templates/playlist_create.html", {'form': form})


def playlist_detail_view(request, pk):
    if request.user.is_authenticated:

        playlist = Playlist.objects.get(pk=pk)
        tracks = playlist.tracks.all()
        return render(
            request,
            "templates/playlist_detail.html",
            {'playlist': playlist, 'tracks': tracks}
            )
    else:
        return redirect('login')


def playlist_add_track_view(request, playlist_pk, track_pk):
    if request.user.is_authenticated:

        track = Track.objects.get(pk=track_pk)
        playlist = Playlist.objects.get(pk=playlist_pk)

        playlist.tracks.add(track)

        return redirect('playlist-detail', pk=playlist.pk)

    else:
        return redirect('login')

# def playlist_add_track_view

# def playlist_remove_track_view


def user_create_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user-detail', username=user.username)
        else:
            return render(
                request, "templates/user_create.html", {'form': form}
                )
    else:
        form = UserCreationForm()
        return render(request, "templates/user_create.html", {'form': form})


def user_detail_view(request, username):
    user = User.objects.get(username=username)
    tracks = Track.objects.filter(artist=user)
    playlists = user.playlist_set.all()
    return render(
        request,
        "templates/user_detail.html",
        {'user': user, 'tracks': tracks, 'playlists': playlists}
        )
