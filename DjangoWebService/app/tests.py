"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase

class ApiVersionTest(TestCase):
    """Tests."""
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ApiVersionTest, cls).setUpClass()
            django.setup()

    def test_get(self):
        """Test Get"""
        response = self.client.get('/')
        self.assertContains(
            response,
            "{\"MyApiVersion\": \"v1.0\"}"
        )

    def test_post(self):
        """Test Post"""
        response = self.client.post(
            '/',
            content_type='application/json',
            data="{\"MyApiVersion\": \"v2.0\"}"
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/')
        self.assertContains(
            response,
            "{\"MyApiVersion\": \"v2.0\"}"
        )
