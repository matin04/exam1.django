from django.urls import path

from .views import *

urlpatterns = [
    path('books/', get_book, name='books'),
    path('create_book/', create_book,name='create_book'),
    path('delete_book/<int:id>/', delete_book,name='delete_book'),
    path('update_book/<int:id>/', update_book,name='update_book'),
]


