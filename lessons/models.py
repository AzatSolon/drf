from django.db import models

NULLEBELL = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название курса")
    photo = models.ImageField(
        upload_to="lessons/course_photo", verbose_name="Превью", **NULLEBELL
    )
    description = models.TextField(verbose_name="Описание")
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="Владелец курса",
        **NULLEBELL,
    )

    def __str__(self):
        return f"{self.title}: {self.description}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название урока")
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание", **NULLEBELL
    )
    prewie = models.ImageField(
        upload_to="lessons/prewies_photo", verbose_name="Превью", **NULLEBELL
    )
    url = models.TextField(verbose_name="Cсылка на видео", **NULLEBELL)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        related_name="lessons",
        **NULLEBELL,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="Владелец урока",
        **NULLEBELL,
    )

    def __str__(self):
        return f"{self.course}/{self.title}: {self.description}, {self.url}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
