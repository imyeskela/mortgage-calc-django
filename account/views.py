from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.viewsets import generics

from .models import User
from .serializers import RegistrationSerializer


class RegistrationApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super(RegistrationApiView, self).create(request, *args, **kwargs)
        return HttpResponseRedirect('http://127.0.0.1:8000/api/v1/account/auth/login/')



