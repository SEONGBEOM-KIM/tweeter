from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "payload",
        "count_likes",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = ("__str__", )
