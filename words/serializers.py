from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Word


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'word', 'times_seen', 'created_at',)
        model = Word

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)