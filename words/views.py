from rest_framework import generics

from .models import Word
from .permissions import IsAuthor
from .serializers import WordSerializer

class WordList(generics.ListCreateAPIView):
    model = Word
    serializer_class = WordSerializer

    def get_queryset(self):
        user = self.request.user
        return user.word_set.all()


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthor,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer