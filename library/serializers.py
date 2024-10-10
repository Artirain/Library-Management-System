from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from .models import Author, Book, FavoriteBook

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password']
            )
            return user
        except IntegrityError:
            raise serializers.ValidationError({"username": ["Пользователь с таким именем уже существует."]})

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'biography', 'date_of_birth', 'date_of_death']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'summary', 'isbn', 'authors', 'publication_date', 'genre']

class FavoriteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteBook
        fields = ['book', 'user']
        extra_kwargs = {'user': {'read_only': True}}  # Делает поле user только для чтения

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user  # Автоматически добавляет пользователя
        return super().create(validated_data)