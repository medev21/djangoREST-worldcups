from django.shortcuts import render
from worlcups.models import Worldcup
from worlcups.permissions import IsOwnerOrReadOnly
from worlcups.serializers import WorldcupSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions, renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response
# Create your views here.


class WorldcupViewSet(viewsets.ModelViewSet):
    queryset = Worldcup.objects.all()
    serializer_class = WorlcupSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @detail_route(renderer_classes = [renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
