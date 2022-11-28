from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('delete_book/<book_id>', views.delete_book, name='delete-book'),
    path('update_book/<book_id>', views.update_book, name='update-book'),
]
