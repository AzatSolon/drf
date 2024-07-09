from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from lessons.models import Lesson, Course, Subscription
from lessons.validators import YouTubeValidation


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YouTubeValidation(field="url")]


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source="lesson_set", many=True)
    lesson_count = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    course_lesson_count = SerializerMethodField()
    course_lessons = SerializerMethodField()

    def get_course_lessons(self, course):
        lessons_set = Lesson.objects.filter(course=course.id)
        return [
            (
                lesson.lesson_name,
                lesson.lesson_description,
                lesson.lesson_url,
                lesson.owner,
            )
            for lesson in lessons_set
        ]

    def get_course_lesson_count(self, course):
        lesson_set = Lesson.objects.filter(course=course.id)
        return lesson_set.count()

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор Подписки"""

    class Meta:
        model = Subscription
        fields = "__all__"
