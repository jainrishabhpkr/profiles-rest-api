from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets , filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import models
from . import permissions

from . import serializers
# Create your views here.


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):

        an_apiview=['apple',
                      'banana',
                      'cat',
                      'dog']
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method':'put andn '})


    def patch(self, request, pk=None):
        return Response({'method':'patch'})


    def delete(self,request, pk=None):
        return Response({'message':'delete'})



class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        a_viewset=['chotu','tanu','tony','pony','sonu','monu']
        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self,request):
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retreive(self, request, pk=None):
        return Response({"http_method":"GET"})

    def update(self, request, pk=None):
        return Response({"http_method":"PUT"})

    def partial_update(self, request, pk=None):
        return Response({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        return Response({"http_method":"DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)

    search_fields  = ('name','email',)


class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedSerializer
    permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)
    queryset = models.ProfileFeed.objects.all()

    def perform_create(self, serializer):
        # sets user profile to logged in user
        serializer.save(user_profile = self.request.user)
