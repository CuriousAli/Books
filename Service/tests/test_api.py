from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Service.models import Book
from Service.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='test book 1', price='22.00', author_name='Ali')
        self.book_2 = Book.objects.create(name='test book 2', price='232.00', author_name='Alqsher')
        self.book_3 = Book.objects.create(name='test book 3 Ali', price='2323.00', author_name='Alina')


    def test_get(self):
        url = reverse('book-list')

        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')

        response = self.client.get(url, data={'price': 2323})
        serializer_data = BooksSerializer([self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


    def test_get_search(self):
        url = reverse('book-list')

        response = self.client.get(url, data={'search': 'Ali'})
        serializer_data = BooksSerializer([self.book_1, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
