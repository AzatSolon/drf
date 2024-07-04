from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User, Payment
from users.serializers import (
    UserSerializer,
    CreateUserSerializer,
    PaymentSerializer,
    MyTokenObtainPairSerializer,
)


class UserRegisterView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(self.request.data["password"])
        user.save()


class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ["payment_method"]
    ordering_fields = ["payments_date"]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
