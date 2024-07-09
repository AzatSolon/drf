from django.urls import path
from rest_framework.routers import SimpleRouter

from lessons.views import (
    CourseViewSet,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonDestroyApiView,
    LessonUpdateApiView,
    LessonCreateAPIView,
    SubscriptionCreateAPIView,
)
from lessons.apps import LessonsConfig

app_name = LessonsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lessons_retrieve"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lessons_create"),
    path(
        "lessons/<int:pk>/delete/",
        LessonDestroyApiView.as_view(),
        name="lessons_delete",
    ),
    path(
        "lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lessons_update"
    ),
    path(
        "subscription/create/",
        SubscriptionCreateAPIView.as_view(),
        name="subscription_create",
    ),
]
urlpatterns += router.urls
