from django.contrib import admin
from .models import Author, Book, FavoriteBook, CustomUser


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'publication_date']

@admin.register(FavoriteBook)
class FavoriteBookAdmin(admin.ModelAdmin):
    list_display = ['user', 'book']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass