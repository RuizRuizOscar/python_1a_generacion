from rest_framework import serializers

from vet.models import PetOwner, Pet, PetDate

class OwnersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name", "email", "phone", "address", "created_at",]

class PetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "name", "type", "owner_id"]

class DatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id", "datetime", "type", "created_at", "pet_id"]