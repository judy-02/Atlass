from django.shortcuts import render  # Not used in this specific view
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser  # Needed for parsing JSON data
from django.http import JsonResponse
from Telescope.models import Telescope  # Import your Telescope model

import ephem  # Import the ephem library for celestial object calculations

@api_view(['GET','POST'])
def search_celestial_object(request):
    "Searches for a celestial object and returns its coordinates."

    # Parse the JSON request data
    try:
        data = JSONParser().parse(request)
        object_name = data.get('object_name')
    except Exception as e:
        return Response({'error': f"Invalid JSON data: {str(e)}"}, status=400)

    # Validate the input (optional)
    if not object_name:
        return Response({'error': 'Missing object name in request body'}, status=400)

    # Use ephem library to calculate coordinates
    try:
        celestial_object = ephem.readdb(object_name)  # Replace with your preferred method for coordinate lookup
        ra = celestial_object.ra  # Right Ascension
        dec = celestial_object.dec  # Declination
        coordinates = {'ra': ra, 'dec': dec}
    except Exception as e:
        return Response({'error': f"Celestial object not found or calculation error: {str(e)}"}, status=404)

    # Return successful response with coordinates
    return Response(coordinates, status=200)


@api_view(['POST'])
def register_telescope(request):
    """Registers a new telescope."""

    try:
        data = JSONParser().parse(request)
        name = data['name']
        manufacturer = data['manufacturer']
        # ... other fields from the request data

        telescope = Telescope.objects.create(
            name=name,
            manufacturer=manufacturer,
            # ... other fields
        )

        return Response({'message': 'Telescope registered successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
