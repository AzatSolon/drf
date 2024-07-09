from django.db import models

from config.settings import AUTH_USER_MODEL

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
    url = models.URLField(
        max_length=200,
        **NULLEBELL,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
    )
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


class Subscription(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="пользователь"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="курс")
    is_subscribe = models.BooleanField(default=False, verbose_name="подписка")

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
