from django.urls import path
from .views import BookView

urlpatterns = [
    path('books', BookView.as_view(), name='book-list'),
    path('books/<int:id>', BookView.as_view(), name='book-detail'),
]