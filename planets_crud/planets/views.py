from rest_framework import generics
from .models import Planet
from .serializers import PlanetSerializer


class PlanetListCreateView(generics.ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class PlanetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
