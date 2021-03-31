from rest_framework import serializers
from django.contrib.auth.models import User

from vet.models import PetOwner, Pet, PetDate, BranchOffice

#Serializers define the API representation

class OwnersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name"]

class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"

# --------------------------------------------------------

class BranchOfficeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOffice
        fields = ["id", "alias"]

class BranchOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOffice
        fields = "__all__"

# --------------------------------------------------------

class PetsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "name"]

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"

# --------------------------------------------------------

class DatesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id", "datetime", "type", "branch_office", "pet"]

class DatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = "__all__"



# --------------------------------------------------------

class OwnerPetsSerializer(serializers.ModelSerializer):
    pets = PetsListSerializer(many=True)
    dates = DatesListSerializer(many=True)
    class Meta:
        model = PetOwner
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "created_at",
            "pets",
            "dates",
        ]

class PetOwnerSerializer(serializers.ModelSerializer):
    owner = OwnersListSerializer()
    class Meta:
        model = Pet
        fields = ["id", "name", "type", "created_at", "owner"]

# --------------------------------------------------------

class BranchOfficeDatesSerializer(serializers.ModelSerializer):
    dates = DatesListSerializer(many=True)
    class Meta:
        model = BranchOffice
        fields = [
            "id",
            "alias",
            "dates",
        ]

# --------------------------------------------------------

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validate_data):
        print(validate_data)
        user = User.objects.create_user(**validate_data)

        return user 

# class OwnersSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PetOwner
#         fields = ["id", "first_name", "last_name", "email", "phone", "address", "created_at",]

# class PetsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Pet
#         fields = ["id", "name", "type", "owner_id"]

# class DatesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PetDate
#         fields = ["id", "datetime", "type", "created_at", "pet_id"]