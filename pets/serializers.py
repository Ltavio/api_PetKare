from rest_framework import serializers
from .models import InformedSex
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer

from .models import Pet
from groups.models import Group
from traits.models import Trait

import ipdb


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=InformedSex.choices,
        default=InformedSex.NOT_INFORMED,
    )
    traits_count = serializers.SerializerMethodField()
    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def get_traits_count(self, obj: Pet) -> int:

        traits = Trait.objects.filter(pets=obj.id)

        return len(traits)

    def create(self, validated_data: dict):

        group_dict = validated_data.pop("group")
        traits_list = validated_data.pop("traits")

        group_obj = Group.objects.get_or_create(**group_dict)[0]
        pet = Pet.objects.create(**validated_data, group=group_obj)

        list = []
        for trait in traits_list:
            trait_obj = Trait.objects.get_or_create(**trait)[0]
            list.append(trait_obj)

        pet.traits.set(list)

        return pet

    def update(self, instance, validated_data: dict):
        group_dict: dict = validated_data.pop("group", None)
        traits_list = validated_data.pop("traits", None)

        if group_dict:
            group_obj = Group.objects.get_or_create(pets=instance)[0]
            for key, value in group_dict.items():
                setattr(group_obj, key, value)
            group_obj.save()

        if traits_list:
            list = []

            for trait in traits_list:
                traits_obj = Trait.objects.get_or_create(**trait)[0]

                for key, value in trait.items():
                    setattr(traits_obj, key, value)

                traits_obj.save()
                list.append(traits_obj)

            instance.traits.set(list)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
