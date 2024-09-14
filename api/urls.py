from django.urls import path
from . import views


urlpatterns = [
    path('', views.search_celestial_object),
    path('\profile', views.register_telescope),
]