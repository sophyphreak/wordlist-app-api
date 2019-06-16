from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Word
from .permissions import IsAuthor
from .serializers import WordSerializer, UserSerializer

class WordViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthor,)
    # queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        user = self.request.user
        return user.word_set.all()

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer