from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from .third_party_api import fetch_movies
from .models import Collection, Movie
from .serializers import CollectionSerializer, LoginSerializer, RegisterSerializer


class RegisterView(APIView):

    @swagger_auto_schema(
        request_body=RegisterSerializer,
        responses={200: RegisterSerializer}
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({'access_token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(APIView):

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: LoginSerializer}
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({'access_token': token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieListView(APIView):
    def get(self, request):
        page = request.query_params.get("page", 1)
        data = fetch_movies(page=page)
        if data:
            return Response(data, status=status.HTTP_200_OK)
        return Response(
            {"error": "Unable to fetch movies"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class CollectionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        collections = Collection.objects.filter(user=request.user)
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CollectionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, collection_uuid):
        # Retrieve and return the Collection instance based on the UUID and the authenticated user
        return get_object_or_404(Collection, uuid=collection_uuid, user=self.request.user)

    def get(self, request, collection_uuid):
        # Retrieve and return details of a specific collection
        collection = self.get_object(collection_uuid)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    def put(self, request, collection_uuid):
        # Update details of a specific collection
        collection = self.get_object(collection_uuid)
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, collection_uuid):
        # Delete a specific collection
        collection = self.get_object(collection_uuid)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)