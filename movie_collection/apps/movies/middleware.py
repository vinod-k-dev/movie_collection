from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response

class RequestCounterMiddleware(MiddlewareMixin):
    def process_request(self, request):
        count = cache.get("request_count", 0)
        cache.set("request_count", count + 1, None)


class ResetRequestCounter(APIView):
    def post(self, request):
        cache.set("request_count", 0, None)
        return Response(
            {"message": "request count reset successfully"}, status=status.HTTP_200_OK
        )


class RequestCountView(APIView):
    def get(self, request):
        count = cache.get("request_count", 0)
        return Response({"requests": count}, status=status.HTTP_200_OK)
