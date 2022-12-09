from django.urls import path
from . import views

urlpatterns = [
    path("pets/", views.PetViews.as_view()),
    path("pets/<int:pet_id>/", views.PetDetailViews.as_view()),
]
