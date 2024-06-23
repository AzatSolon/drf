from django.db import models

from users.models import NULLEBELL


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название курса")
    photo = models.ImageField(
        upload_to="lessons/course_photo", verbose_name="превью", **NULLEBELL
    )
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название урока")
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание"
    )
    prewie = models.ImageField(
        upload_to="lessons/prewies_photo", verbose_name="превью", **NULLEBELL
    )
    url = models.TextField(verbose_name="Cсылка на видео", **NULLEBELL)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        related_name="lessons",
        **NULLEBELL
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
