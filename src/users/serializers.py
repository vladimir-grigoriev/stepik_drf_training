from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = User.objects.create(username="NewUser", **validated_data)
        instance.set_username()
        instance.set_password(validated_data["password"])
        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "phone",
            "adress",
        ]
        read_only_fields = ("id", "username")
