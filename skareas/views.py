from django.shortcuts import render
from skareas.serializers import UserSerializer

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions

import skareas.models as sm
import skareas.serializers as ss


# Create your views here.
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework.decorators import detail_route

class SkiAreaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = sm.SkiArea.objects.all()
    serializer_class = ss.SkiAreaSerializer

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            # no anonymous editing allowed
            return

        serializer.save(owner=self.request.user)
