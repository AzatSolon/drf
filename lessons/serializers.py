from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lessons.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonDetailSerializer(ModelSerializer):
    count_lessons_in_course = SerializerMethodField()
    course = CourseSerializer()

    def get_count_lessons_in_course(self, lesson):
        return Lesson.objects.filter(course=lesson.course).count()

    class Meta:
        model = Lesson
        fields = "__all__"
