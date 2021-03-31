from django.urls import path, include

from .views import ListOwnersAPIView,   RetrieveOwnersAPIView,  CreateOwnersAPIView,    UpdateOwnersAPIView,    DestroyOwnersAPIView
from .views import ListPetsAPIView,     RetrievePetsAPIView,    CreatePetsAPIView,      UpdatePetsAPIView,      DestroyPetsAPIView
from .views import RetrieveOwnerPetsAPIView,    RetrievePetsOwnerAPIView
from .views import ListBranchOfficesAPIView,    CreateBranchOfficesAPIView
from .views import CreateDatesAPIView
from .views import RetrieveBranchOfficeDatesAPIView
from .views import RetrieveUpdatePetsAPIView
    # Users
from .views import CreateUsersAPIView

from rest_framework.authtoken import views

urlpatterns = [
    path("owners/", ListOwnersAPIView.as_view(), name="list-owners"),
    path("owners/create/", CreateOwnersAPIView.as_view(), name="create-owners"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="retrieve-owners"),
    path("owners/<int:pk>/update/", UpdateOwnersAPIView.as_view(), name="update-owners"),
    path("owners/<int:pk>/destroy/", DestroyOwnersAPIView.as_view(), name="destroy-owners"),
    
    path("pets/", ListPetsAPIView.as_view(), name="list-pets"),
    path("pets/create/", CreatePetsAPIView.as_view(), name="create-pets"),
    path("pets/<int:pk>/", RetrievePetsAPIView.as_view(), name="retrieve-pets"),
    path("pets/<int:pk>/update/", UpdatePetsAPIView.as_view(), name="update-pets"),
    path("pets/<int:pk>/destroy/", DestroyPetsAPIView.as_view(), name="destroy-pets"),

    path("owners/<int:pk>/pets/", RetrieveOwnerPetsAPIView.as_view(), name="retrieve-owner-pets"),
    path("pets/", ListPetsAPIView.as_view(), name="list-pets"),
    path("pets/<int:pk>/", RetrievePetsOwnerAPIView.as_view(), name="retrieve-pets-owner"),
    path("pets/<int:pk>/retrieve-update/", RetrieveUpdatePetsAPIView.as_view(), name="retrieve-update-pets"),

    path("users/create/", CreateUsersAPIView.as_view(), name="create-users"),
    path("users/login/", views.obtain_auth_token, name="login-users"), # si no tiene token lo crea
    path("dates/create/", CreateDatesAPIView.as_view(), name="create-dates"),

    path("branchoffices/", ListBranchOfficesAPIView.as_view(), name="list-branch-offices"),
    path("branchoffices/create/", CreateBranchOfficesAPIView.as_view(), name="create-branch-offices"),
    path("branchoffices/<int:pk>/dates/", RetrieveBranchOfficeDatesAPIView.as_view(), name="retrieve-branch-offices-dates"),
]

# http://127.0.0.1:8000/api/owners/
# http://127.0.0.1:8000/api/owners/2/
# http://127.0.0.1:8000/api/owners/create/




# from rest_framework import routers
# from .views import OwnersViewSet, PetsViewSet, DatesViewSet

# router = routers.DefaultRouter()
# router.register(r"owners", OwnersViewSet)
# router.register(r"pets", PetsViewSet)
# router.register(r"dates", DatesViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]