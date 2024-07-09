from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lessons.paginators import CustomPaginator
from lessons.models import Course, Lesson, Subscription
from lessons.serializers import (
    CourseSerializer,
    LessonSerializer,
    CourseDetailSerializer,
    SubscriptionSerializer,
)
from users.permissions import IsModer, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CustomPaginator

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(owner=self.request.user)

        elif self.request.user.is_staff:
            return Course.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [
                ~IsModer,
                IsAuthenticated,
            ]
        elif self.action == "destroy":
            self.permission_classes = [
                ~IsModer,
                IsOwner,
            ]
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = [
                IsModer | IsOwner,
            ]
        elif self.action == "list":
            self.permission_classes = [IsModer, IsAuthenticated]
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [
        ~IsModer,
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListApiView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CustomPaginator
    permission_classes = [
        IsModer,
    ]


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModer | IsOwner]


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModer | IsOwner]


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner, IsAuthenticated]


class SubscriptionCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course = get_object_or_404(Course, pk=course_id)

        subscription, created = Subscription.objects.get_or_create(
            user=user, course=course
        )
        if not created:
            subscription.delete()
            message = "Подписка удалена"
        else:
            message = "Подписка добавлена"

        return Response({"message": message})
