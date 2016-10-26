from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Test


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class TestSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Test.objects.create(**validated_data)

    class Meta:
        model = Test
        fields = ('username', 'email', 'password')
