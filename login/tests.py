from django.test import TestCase
from django.test.client import Client
from despegar.models import *
from django.contrib.auth.models import User
import json
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class UserTestCase(TestCase):

    def setUp(self):
        user = User(
            username='eltomas',
            password='tomii123',
            # password2='tomii123',
            email='tomasito@gmail.com',
            first_name='Tomas',
            last_name='Alvarez'
        )
        user.set_password('tomii123')
        user.save()

    def test_signup_user(self):
        """Check if we can create an user"""
        client = APIClient()
        response = client.post(
            '/register/', {
                "username": "tomasito",
                "password": "tomasito",
                "password2": "tomasito",
                "first_name": "Tomas",
                "last_name": "Alvarez",
                "email": "tomasito@tomas.com"
            },

            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {
            "username": "tomasito",
                        "email": "tomasito@tomas.com",
                        "first_name": "Tomas",
                        "last_name": "Alvarez"})

    def test_login_user(self):
        client = APIClient()
        response = client.post(
            '/login/',{
                "username": "eltomas",
                "password": "tomii123"
            },
            
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = json.loads(response.content) 
        self.assertIn('access', result)
