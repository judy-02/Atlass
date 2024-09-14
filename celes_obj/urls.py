from django.urls import path
from .views import search_celestial_object

urlpatterns = [
    path('api/celestial-objects/search/', search_celestial_object),
]