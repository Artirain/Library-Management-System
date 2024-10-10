from celery import shared_task
from django.utils import timezone
from .models import Book
from django.contrib.auth.models import User


@shared_task
def notify_new_books():
    last_24_hours = timezone.now() - timezone.timedelta(days=1)  # Получаем книги, добавленные за последние 24 часа
    new_books = Book.objects.filter(created_at__gte=last_24_hours)


    if not new_books.exists():
        return  # Нет новых книг, ничего не делаем

    # Формируем сообщение
    message = "Список новых книг за последние 24 часа:\n"
    for book in new_books:
        message += f"{book.title} - {book.summary}\n"

    print(message)

@shared_task
def notify_anniversary_books():
    today = timezone.now().date()
    anniversary_years = [5, 10, 20]  # Юбилейные годы
    anniversary_books = []

    for years in anniversary_years:
        anniversary_date = today - timezone.timedelta(days=years * 365)  #365 дней в году
        books = Book.objects.filter(publication_date=anniversary_date)
        anniversary_books.extend(books)

    # Если нет юбилейных книг, просто завершаем выполнение задачи
    if not anniversary_books:
        return

    message = "Список юбилейных книг:\n"
    for book in anniversary_books:
        message += f"{book.title} - {book.summary}\n"

    print(message)