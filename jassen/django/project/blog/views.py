from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import AnimeSerializer
from .models import Animme


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Animme.objects.all().order_by('-date_created')
    serializer_class = AnimeSerializer

