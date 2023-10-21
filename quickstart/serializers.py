from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework import serializers
from product.models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CadeauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'