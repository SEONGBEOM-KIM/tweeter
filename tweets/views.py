from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from users.models import User
from .models import Tweet
from .serializers import TweetSerializer


class Tweets(APIView):

    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data)

        


class TweetDetail(APIView):

    def get(self, request, user_id):
        try:
          user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
          raise NotFound
        tweets = Tweet.objects.filter(user=user_id)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)


