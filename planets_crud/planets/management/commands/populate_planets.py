from django.core.management.base import BaseCommand
import requests
from ...models import Planet


class Command(BaseCommand):
    help = 'Populate the database with data from SWAPI GraphQL'

    def handle(self, *args, **kwargs):
        # Define the GraphQL query
        graphql_query = '''
        {
          allPlanets {
            planets {
              name
              population
              terrains
              climates
            }
          }
        }
        '''

        # URL of the SWAPI GraphQL API
        api_url = 'https://swapi-graphql.netlify.app/.netlify/functions/index'

        # Send a POST request to the API
        response = requests.post(api_url, json={'query': graphql_query})

        if response.status_code == 200:
            data = response.json()
            planets = data.get('data', {}).get('allPlanets', {}).get('planets', [])

            for planet_data in planets:
                # Create or update the Planet object in your database
                Planet.objects.update_or_create(
                    name=planet_data['name'],
                    defaults={
                        'population': planet_data['population'],
                        'terrains': planet_data['terrains'],
                        'climates': planet_data['climates'],
                    }
                )

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with SWAPI data'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from SWAPI GraphQL'))
