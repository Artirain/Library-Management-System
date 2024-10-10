from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegistrationAPIView, LoginAPIView, LogoutAPIView,
    AuthorListCreateView, AuthorDetailView,
    BookListCreateView, BookDetailView,
    FavoriteBookListCreateView, FavoriteBookDeleteView, ClearFavoriteBooksView
)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # CRUD для авторов
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # CRUD для книг
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),


    # Избранные книги
    path('favorites/', FavoriteBookListCreateView.as_view(), name='favorite-list-create'),
    path('favorites/<int:pk>/', FavoriteBookDeleteView.as_view(), name='favorite-delete'),
    path('favorites/clear-all/', ClearFavoriteBooksView.as_view(), name='favorites-clear-all'),
]
