from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UserRegisterView,
    UserUpdateView,
    UserRetrieveView,
    UserListView,
    UserDeleteView,
    PaymentViewSet,
)

app_name = UsersConfig.name
router = DefaultRouter()
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [
    path("create/", UserRegisterView.as_view(), name="users_create"),
    path("detail/<int:pk>/", UserRetrieveView.as_view(), name="user_detail"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
    path("users_list/", UserListView.as_view(), name="users_list"),
    path(
        "token/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
] + router.urls
