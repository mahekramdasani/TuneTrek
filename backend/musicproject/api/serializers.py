# api/serializers.py 
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserLike

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return super(UserSerializer, self).create(validated_data)

class UserLikeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='email')

    class Meta:
        model = UserLike
        fields = ('user', 'liked_on')