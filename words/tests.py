from django.test import TestCase
from django.contrib.auth.models import User

from .models import Word


class WordlistTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        # Create a wordlist word
        test_word = Word.objects.create(
            author=testuser1, word="庄子", times_seen=11)
        test_word.save()

    def test_word_content(self):
        word = Word.objects.get(id=1)
        expected_author = f'{word.author}'
        expected_word = f'{word.word}'
        expected_times_seen = f'{word.times_seen}'
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_word, '庄子')
        self.assertEqual(expected_times_seen, '11')