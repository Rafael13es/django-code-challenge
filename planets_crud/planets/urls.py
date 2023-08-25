from django.urls import path
from .views import PlanetListCreateView, PlanetRetrieveUpdateDestroyView

urlpatterns = [
    path('planets/', PlanetListCreateView.as_view(), name='planet-list-create'),
    path('planets/<int:pk>/', PlanetRetrieveUpdateDestroyView.as_view(), name='planet-retrieve-update-destroy'),
]
