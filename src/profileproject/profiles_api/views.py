from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    def get(self,request,format=None):

        an_apiview=['apple',
                      'banana',
                      'cat',
                      'dog']
        return Response({'message':'hello','an_apiview':an_apiview})
        
