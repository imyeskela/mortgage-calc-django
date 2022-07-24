from rest_framework import serializers

from .models import Mortgage

BANK_NAME_CHOICES = (
    ('SBER'),
    ('VTB'),
    ('RAIFEZENBANK'),
    ('ROSBANK'),
    ('UNICREDITBANK'),
    ('CITYBANK'),
    ('DOICHEBANK'),
    ('RNBANK')
)


class MortgageSerializer(serializers.Serializer):
    price = serializers.IntegerField()
    initial_fee = serializers.IntegerField()
    term = serializers.IntegerField()
    bank_name_filter = serializers.CharField(max_length=100, required=False, default=None)
    rate_min_filter = serializers.FloatField(required=False, default=None)
    rate_max_filter = serializers.FloatField(required=False, default=None)



