from rest_framework import serializers
from . import models
from project.apps.security.serializers import UserDetailSerializer


# class ItemsSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.Item
#         fields = '__all__'


class ObjectSerializer(serializers.ModelSerializer):
    owner = UserDetailSerializer(read_only=True)
    class Meta:
        model = models.Object
        fields = '__all__'
        # read_only_fields = ('owner', )
