from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    pass


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    biography = models.TextField(verbose_name="Биография")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    date_of_death = models.DateField(null=True, blank=True, verbose_name="Дата смерти")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    summary = models.TextField(verbose_name="Краткое содержание")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="Уникальный номер ISBN")
    authors = models.ManyToManyField(Author, related_name='books', verbose_name="Авторы")
    publication_date = models.DateField(verbose_name="Дата публикации")
    genre = models.CharField(max_length=100, verbose_name="Жанр")

    def __str__(self):
        return self.title


class FavoriteBook(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorite_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'

