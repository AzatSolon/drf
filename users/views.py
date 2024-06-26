from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from users.models import User, Payment
from users.serializers import UserSerializer, CreateUserSerializer, PaymentSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


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
