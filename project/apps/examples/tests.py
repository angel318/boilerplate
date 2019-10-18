# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from ..security.models import User
from django.urls import reverse
from .models import Object
from .serializers import ObjectSerializer

# Create your tests here.

class GetAllObjectTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.valid_login = {
        'email': 'admin@admin.com',
        'password': 'admin123'
        }
        response = self.client.post('/v1/auth/token/',data=json.dumps(self.valid_login), content_type='application/json')
        self.access = response.data.get('access')
        Object.objects.create(name="Objeto numero 1", owner=self.user)
        Object.objects.create(name="Objeto numero 2", owner=self.user)
        Object.objects.create(name="Objeto numero 3", owner=self.user)
        

    
    def test_get_all_puppies(self):
        ##self.client.force_login(user=)
        response = self.client.get(reverse('objects-list'), HTTP_AUTHORIZATION='Bearer {}'.format(self.access))
        # get data from db
        objects = Object.objects.all()
        serializer = ObjectSerializer(objects, many=True)
        data = response.data.get('data')
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

