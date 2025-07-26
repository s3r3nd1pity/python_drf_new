from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.user.models import ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'created_at', 'updated_at','name','surname', 'age', 'user_id')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'last_login', 'is_staff', 'is_superuser',"is_active", 'last_login', 'created_at', 'updated_at','profile')
        read_only_fields = ('created_at', 'updated_at', "id", 'is_staff',"is_active", 'is_superuser', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
    def create(self, validated_data:dict):
        profile=validated_data.pop('profile')
        user=get_user_model().objects.create_user(**validated_data)
        ProfileModel.objects.create(user=user, **profile)
        return user
