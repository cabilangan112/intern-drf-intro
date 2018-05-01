from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Anime,Website,Breed
from .serializers import (AnimeSerializer,
	                      WebsiteSerializer,
	                      BreedSerializer)



class breedViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Breed.objects.all()
        serializer = BreedSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Breed.objects.all()
        serializer = BreedSerializer(queryset, many=True)
        return Response(serializer.data)


class AnimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Anime.objects.all().order_by('-date_created')
    serializer_class = AnimeSerializer

class WebsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Website.objects.all().order_by('-date_created')
    serializer_class = WebsiteSerializer

 