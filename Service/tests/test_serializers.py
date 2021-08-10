from unittest import TestCase

from Service.models import Book
from Service.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='test book 1', price=22)
        book_2 = Book.objects.create(name='test book 2', price=232)
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'test book 1',
                'price': '22.00'
            },
            {
                'id': book_2.id,
                'name': 'test book 2',
                'price': '232.00'
            }
        ]
        self.assertEqual(expected_data, data)
