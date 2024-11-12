from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
from .models import Tweet


class TweetSerializer(ModelSerializer):

  user = UserSerializer(read_only=True)

  class Meta:
    model = Tweet
    fields = (
        "payload",
        "user",
        "count_likes",
        "created_at",
    )
