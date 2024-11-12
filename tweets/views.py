from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Tweet
from .serializers import TweetSerializer


class Tweets(APIView):

    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            tweet = serializer.save(
                user=request.user
            )
            serializer = TweetSerializer(tweet)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
        


class TweetDetail(APIView):

    def get(self, request, pk):
        try:
          tweet = Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
          raise NotFound
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            tweet = Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound
        serializer = TweetSerializer(tweet, data=request.data, partial=True,)
        if serializer.is_valid():
            updated_tweet = serializer.save()
            serializer = TweetSerializer(updated_tweet)
            return Response(serializer.data)
        else:
            return Response(serializer.error)

    def delete(self, request, pk):
        try:
            tweet = Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)

