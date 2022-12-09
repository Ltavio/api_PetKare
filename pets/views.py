from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404


from .models import Pet
from .serializers import PetSerializer


class PetViews(APIView):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()

        pet_serializer = PetSerializer(pets, many=True)

        return Response(pet_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        pet_serializer = PetSerializer(data=request.data)

        pet_serializer.is_valid(raise_exception=True)

        pet_serializer.save()

        return Response(pet_serializer.data, status.HTTP_201_CREATED)


class PetDetailViews(APIView):
    def patch(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        pet_serializer = PetSerializer(pet, data=request.data, partial=True)

        pet_serializer.is_valid(raise_exception=True)

        pet_serializer.save()

        return Response(pet_serializer.data, status.HTTP_200_OK)
