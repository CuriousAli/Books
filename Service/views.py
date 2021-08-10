from rest_framework.viewsets import ModelViewSet

from Service.models import Book
from Service.serializers import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
