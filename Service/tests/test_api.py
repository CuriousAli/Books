import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Service.models import Book, UserBookRelation
from Service.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'test_user')
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


    def test_post(self):
        url = reverse('book-list')

        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


    def test_create(self):

        url = reverse('book-list')
        data = {
                'name': 'test book pythonn',
                'price': '2222.00',
                'author_name': 'Rossum'
            }
        self.client.force_login(self.user)
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def test_update(self):

        url = reverse('book-detail', args=(self.book_1.id,))
        data = {
                'name': self.book_1.name,
                'price': 550,
                'author_name': self.book_1.author_name
            }
        self.client.force_login(self.user)
        json_data = json.dumps(data)
        response = self.client.put(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)


class BooksRelationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'test_user')
        self.user2 = User.objects.create(username='test_user2')
        self.book_1 = Book.objects.create(name='test book 1', price='22.00', author_name='Ali')
        self.book_2 = Book.objects.create(name='test book 2', price='232.00', author_name='Alqsher')

    def test_like(self):
        url = reverse('userbookrelation-detail', args=(self.book_1.id,))

        data = {
            'like': True,
        }

        self.client.force_login(self.user)
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertTrue(relation.like)

        data = {
            'in_bookmarks': True,
        }
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertTrue(relation.in_bookmarks)


    def test_rate(self):
        url = reverse('userbookrelation-detail', args=(self.book_1.id,))

        data = {
            'rate': 4,
        }

        self.client.force_login(self.user)
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertEqual(4, relation.rate)

    def test_rate_wrong(self):
        url = reverse('userbookrelation-detail', args=(self.book_1.id,))

        data = {
            'rate': 7,
        }

        self.client.force_login(self.user)
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertEqual(4, relation.rate)

