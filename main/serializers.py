from rest_framework import serializers

from .models import Mortgage


class MortgageSerializer(serializers.Serializer):
    price = serializers.IntegerField()
    initial_fee = serializers.IntegerField()
    term = serializers.IntegerField()
