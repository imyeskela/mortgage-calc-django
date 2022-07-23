import random

from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import MortgageSerializer
from .models import Mortgage
from .services import get_mortgage_list, save_data


class MortgageViewSet(ViewSet):
    def create(self, request):
        serializer = MortgageSerializer(data=request.data)
        if serializer.is_valid():
            price = int(serializer.validated_data.get("price"))
            initial_fee = int(serializer.validated_data.get("initial_fee"))
            term = int(serializer.validated_data.get("term"))
            mortgage_data = get_mortgage_list(price=price, initial_fee=initial_fee, term=term)
            save_data(mortgage_data)
            return Response(mortgage_data)


    # def list(self, request):
    #     serializer = MortgageSerializer(data=request.data)
    #     price = int(serializer.validated_data.get("price"))
    #     initial_fee = int(serializer.validated_data.get("initial_fee"))
    #     term = int(serializer.validated_data.get("term"))
    #     return Response(payment_formula(price=price, initial_fee=initial_fee, term=term))


