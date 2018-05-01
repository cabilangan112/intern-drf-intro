from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import AnimeSerializer
from .models import Anime


class AnimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Anime.objects.all().order_by('-date_created')
    serializer_class = AnimeSerializer

