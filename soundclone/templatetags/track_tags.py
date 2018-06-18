from django import template

register = template.Library()

@register.filter(name='is_liked_by')
def is_liked_by(track, user):
    return track.is_liked_by(user)