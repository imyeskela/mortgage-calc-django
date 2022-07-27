from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, validators=[validate_password])
    password_again = serializers.CharField(write_only=True, max_length=100)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_again', 'first_name', 'last_name', ]

    def validate(self, data):
        if data['password'] != data['password_again']:
            raise serializers.ValidationError('Password does not match')
        return data

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
