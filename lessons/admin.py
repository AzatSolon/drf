from django.contrib import admin
from lessons.models import Course, Lesson, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "photo"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "url", "prewie", "course"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["pk", "user", "course", "is_subscribe"]
