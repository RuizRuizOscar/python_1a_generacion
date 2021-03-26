from rest_framework import viewsets

from vet.models import PetOwner, Pet, PetDate
from .serializers import OwnersSerializer, PetsSerializer, DatesSerializer
from django.shortcuts import render

# Create your views here.
class OwnersViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo PetOwners.
    """
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class PetsViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo Pets.
    """

    queryset = Pet.objects.all().order_by("created_at")
    serializer_class = PetsSerializer

class DatesViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo Dates.
    """

    queryset = PetDate.objects.all().order_by("created_at")
    serializer_class = DatesSerializer