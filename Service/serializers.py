from rest_framework.serializers import ModelSerializer

from Service.models import Book


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
