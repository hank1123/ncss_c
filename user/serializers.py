from .models import Users, Roles
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('__all__')

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('__all__')