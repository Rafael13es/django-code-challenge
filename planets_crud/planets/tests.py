import json
from os.path import join
from http import HTTPStatus

from django.conf import settings
from django.test import TestCase, RequestFactory
from rest_framework.test import APIClient
from rest_framework import status
from .views import PlanetListCreateView


class PlanetViewTests(TestCase):
    test_fixtures = [
        'planets',
    ]
    test_fixtures_list = []
    path_to_fixtures = join(str(settings.BASE_DIR), 'planets/fixtures/')
    for test_fixture in test_fixtures:
        test_fixtures_list.append(path_to_fixtures + '{}.json'.format(test_fixture))
    fixtures = test_fixtures_list

    def setUp(self):
        self.client = APIClient()
        self.factory = RequestFactory()

    def test_list_planets(self):
        request = self.factory.get('/api/planets/')
        response = PlanetListCreateView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('name'), 'Tatooine')

    def test_create_planet(self):
        data = json.dumps({
            'name': 'Test Planet',
            'population': 1000,
            'terrains': ['Desert', 'Forest'],
            'climates': ['Hot', 'Moderate'],
        })
        response = self.client.post('/api/planets/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, HTTPStatus.CREATED._value_)
        self.assertEqual(response.data.get('name'), 'Test Planet')

    def test_retrieve_planet(self):
        data = json.dumps({
            'name': 'Test Planet',
            'population': 1000,
            'terrains': ['Desert', 'Forest'],
            'climates': ['Hot', 'Moderate'],
        })
        response = self.client.post('/api/planets/', data=data, content_type='application/json')
        new_response = self.client.get(f'/api/planets/{response.data.get("id")}/')
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.data.get('name'), 'Test Planet')

    def test_update_planet(self):
        planet = json.dumps({
            'name': 'Test Planet',
            'population': 1000,
            'terrains': ['Desert', 'Forest'],
            'climates': ['Hot', 'Moderate'],
        })
        response = self.client.post('/api/planets/', data=planet, content_type='application/json')
        data = json.dumps({'name': 'Updated Planet'})
        new_response = self.client.put(
            f'/api/planets/{response.data.get("id")}/', data=data, content_type='application/json')
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.data.get('name'), 'Updated Planet')

    def test_delete_planet(self):
        data = json.dumps({
            'name': 'Test Planet',
            'population': 1000,
            'terrains': ['Desert', 'Forest'],
            'climates': ['Hot', 'Moderate'],
        })
        response = self.client.post('/api/planets/', data=data, content_type='application/json')
        new_response = self.client.delete(f'/api/planets/{response.data.get("id")}/')
        self.assertEqual(new_response.status_code, status.HTTP_204_NO_CONTENT)
