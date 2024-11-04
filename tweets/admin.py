from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):
    title = "Contain 'Elon Musk'"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("elon_musk", "Elon Musk"),
        ]

    def queryset(self, request, tweets):
        word = self.value()
        if word:
            return tweets.filter(payload__contains=word)
        else:
            tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "payload",
        "count_likes",
    )

    list_filter = (
        WordFilter,
        "created_at",
    )

    search_fields = (
        "payload",
        "user__username",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = ("__str__", )

    list_filter = ("created_at", )

    search_fields = ("user__username", )
