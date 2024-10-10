from django.test import TestCase
from .models import Author

class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(first_name="Тест", last_name="Пользователь")

    def test_author_creation(self):
        author = Author.objects.get(first_name="Тест")
        self.assertEqual(author.last_name, "Пользователь")