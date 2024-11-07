from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from users.models import User


@api_view(["GET"])
def detail(request, user_id):
  if request.method == "GET":
    try:
      user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
      raise NotFound
    tweets = Tweet.objects.filter(user=user_id)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)
