from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from .models import User
from .serializers import UserSerializer


class Users(APIView):

  def get(self, request):
    all_users = User.objects.all()
    serializer = UserSerializer(
        all_users,
        many=True,
    )
    return Response(serializer.data)

class UserDetail(APIView):

  def get(self, request, pk):
    try:
      user = User.objects.get(pk=pk)
    except User.DoesNotExist:
      raise NotFound
    serializer = UserSerializer(user)
    return Response(serializer.data)

class UserTweet(APIView):

  def get(self, request, pk):
      try:
        user = User.objects.get(pk=pk)
      except User.DoesNotExist:
        raise NotFound
      tweets = Tweet.objects.filter(user=pk)
      serializer = TweetSerializer(tweets, many=True,)
      return Response(serializer.data)