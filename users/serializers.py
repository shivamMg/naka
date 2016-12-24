from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    # Not using ModelSerializer so to give better error message
    username = serializers.SlugField(
        max_length=20,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='Username already taken.')]
    )
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
