from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.viewsets import generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import RegistrationSerializer, UserSerializer


class RegistrationApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super(RegistrationApiView, self).create(request, *args, **kwargs)
        return HttpResponseRedirect('http://127.0.0.1:8000/api/v1/account/auth/login/')


class UserApiView(APIView):
    def get(self, request, *args, **kwargs):
        if str(kwargs['user_id']) == str(request.user.pk):
            user = get_object_or_404(User, pk=kwargs['user_id'])
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'oops ('})