from rest_framework import serializers

from .models import Mortgage


class MortgageSerializer(serializers.Serializer):
    price = serializers.IntegerField()
    initial_fee = serializers.IntegerField()
    term = serializers.IntegerField()

    # def create(self, validated_data):
    #     # price = int(validated_data["price"])
    #     # initial_fee = int(validated_data["initial_fee"])
    #     # term = int(validated_data["term"])
    #     pass
    #     return Mortgage.objects.create()
