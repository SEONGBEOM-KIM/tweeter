from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "payload",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = ("__str__", )
