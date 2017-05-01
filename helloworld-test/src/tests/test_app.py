import unittest
from requests import get
import json

class TestApp(unittest.TestCase):
    def test_connectivity(self):
        self.assertTrue(get(URL).ok)

    def test_jsonresponse(self):
        response = get(URL).json()
        self.assertIn('greeting', response, 'should greet')
        self.assertEqual(response['greeting'], 'Hello')

class TestAppError(unittest.TestCase):
    def test_invalidpage(self):
        response = get(URL + '/invalidpage')
        self.assertFalse(response.ok)
        response = response.json()
        self.assertIn('message', response, 'should contain message')


