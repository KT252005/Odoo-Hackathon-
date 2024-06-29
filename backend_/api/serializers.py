from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField(default=False)
    is_recycler = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_admin', 'is_recycler']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extract is_admin and is_recycler from validated_data if present, defaults to False
        is_admin = validated_data.pop('is_admin', False)
        is_recycler = validated_data.pop('is_recycler', False)

        # Create the user with User.objects.create_user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_admin=is_admin,
            is_recycler=is_recycler
        )
        return user
