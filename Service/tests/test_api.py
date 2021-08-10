from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Service.models import Book
from Service.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='test book 1', price='22.00')
        book_2 = Book.objects.create(name='test book 2', price='232.00')
        url = reverse('book-list')

        response = self.client.get(url)
        serializer_data = BooksSerializer([book_1, book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

