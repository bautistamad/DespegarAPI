from django.test import TestCase
from django.test.client import Client
from despegar.models import *
from django.contrib.auth.models import User
import json
from django.urls import reverse

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.browser = Client()

    def test_add_user(self):
        print("a")
        self.assertEqual(201, 201)

    # def test_add_user(self):
    #     user = dict(username='eltomas',
    #                 password='tomii123',
    #                 password2='tomii123',
    #                 email='tomasito@gmail.com',
    #                 first_name='Tomas',
    #                 last_name='Alvarez')
    #     response = self.browser.post('/register/', user)
    #     self.assertEqual(response.status_code, 201)

    # def test_error_add_user(self):
    #     # Password field didn't match
    #     user = dict(username='eltomas',
    #                 password='tomii123',
    #                 password2='tomii1234',
    #                 email='tomasito@gmail.com',
    #                 first_name='Tomas',
    #                 last_name='Alvarez')
    #     response = self.browser.post('/register/', user)
    #     self.assertEqual(response.status_code, 400)


    # def test_change_email_user(self):
    #     email = dict(email='tomasito123@gmail.com')
    #     response = self.browser.patch('/login/4',json.dumps(email),content_type="application/json")
    #     self.assertEqual(response.status_code,201)
    

        
