from rest_framework import serializers
from .models import Word


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'word', 'times_seen', 'created_at',)
        model = Word