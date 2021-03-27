from rest_framework import serializers

from vet.models import PetOwner, Pet, PetDate

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

class PetsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "name"]

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"

# --------------------------------------------------------

class OwnerPetsSerializer(serializers.ModelSerializer):
    pets = PetsListSerializer(many=True)
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
            
        ]

class PetOwnerSerializer(serializers.ModelSerializer):
    owner = OwnersListSerializer()
    class Meta:
        model = Pet
        fields = ["id", "name", "type", "created_at", "owner"]


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