from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from api.apis import serializers
from api import models

class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='example',password='NewPassword@123')
        self.token=Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.stream=models.StreamPlatform.objects.create(name='Netflix',about='#1 Streaming Platform',website='https://www.netflix.com')
        
    def test_streamplatform(self):
        data={
            'name':'netflix',
            'about':"#1 Streaming Platform",
            "website":"https://www.netflix.com"
        }
        response=self.client.post(reverse('stream'))
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
        
    def test_streamplatform_list(self):
        response=self.client.get(reverse('stream'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_streamplatform_ind(self):
        response=self.client.get(reverse('stream-details',args=(self.stream.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)