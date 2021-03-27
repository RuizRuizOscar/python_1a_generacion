from rest_framework import generics
from vet.models import PetOwner, Pet, PetDate
from django.shortcuts import render
from .serializers import OwnersListSerializer,  OwnersSerializer
from .serializers import PetsListSerializer,    PetsSerializer
from .serializers import OwnerPetsSerializer,   PetOwnerSerializer

# # Create your views here.

class ListOwnersAPIView(generics.ListAPIView):
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer

class CreateOwnersAPIView(generics.CreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class UpdateOwnersAPIView(generics.UpdateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class DestroyOwnersAPIView(generics.DestroyAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

# -----------------------------------------------------------

class RetrieveOwnerPetsAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnerPetsSerializer

class RetrievePetsOwnerAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetOwnerSerializer

# -----------------------------------------------------------

class ListPetsAPIView(generics.ListAPIView):
    queryset = Pet.objects.all().order_by("id")
    serializer_class = PetsListSerializer

class CreatePetsAPIView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class RetrievePetsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class UpdatePetsAPIView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class DestroyPetsAPIView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer




# GenericViews

#from rest_framework import viewsets
# from .serializers import OwnersSerializer, PetsSerializer, DatesSerializer
# class OwnersViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet del modelo PetOwners.
#     """
#     queryset = PetOwner.objects.all()
#     serializer_class = OwnersSerializer

# class PetsViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet del modelo Pets.
#     """

#     queryset = Pet.objects.all().order_by("created_at")
#     serializer_class = PetsSerializer

# class DatesViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet del modelo Dates.
#     """

#     queryset = PetDate.objects.all().order_by("created_at")
#     serializer_class = DatesSerializer