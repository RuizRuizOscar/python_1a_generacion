from rest_framework import generics
from django.shortcuts import render
from vet.models import PetOwner, Pet, PetDate, BranchOffice
from django.contrib.auth.models import User

from .serializers import OwnersListSerializer,  OwnersSerializer
from .serializers import PetsListSerializer,    PetsSerializer
from .serializers import OwnerPetsSerializer,   PetOwnerSerializer
from .serializers import DatesSerializer
from .serializers import BranchOfficeListSerializer, BranchOfficeSerializer
from .serializers import BranchOfficeDatesSerializer, DatesListSerializer
from .serializers import UsersSerializer
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

class RetrieveUpdatePetsAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

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

# -----------------------------------------------------------

class ListBranchOfficesAPIView(generics.ListAPIView):
    queryset = BranchOffice.objects.all().order_by("id")
    serializer_class = BranchOfficeListSerializer

class CreateBranchOfficesAPIView(generics.CreateAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeSerializer

# -----------------------------------------------------------

class CreateDatesAPIView(generics.CreateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer

# -----------------------------------------------------------
# Ejercicio 4
class RetrieveBranchOfficeDatesAPIView(generics.RetrieveAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeDatesSerializer

# -----------------------------------------------------------

class CreateUsersAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

# class CreateDateAPIView(generics.RetrieveAPIView):
#     queryset = PetDate.objects.all()
#     serializer_class = PetOwnerSerializer*****

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