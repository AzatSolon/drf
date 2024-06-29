from django.contrib.auth.models import AbstractUser
from django.db import models

from lessons.models import Course, Lesson

NULLEBELL = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(max_length=45, **NULLEBELL, verbose_name="Телефон")
    city = models.CharField(max_length=60, verbose_name="Город", **NULLEBELL)
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", **NULLEBELL
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [("cash", "наличные"), ("card", "банковский перевод")]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь"
    )
    payments_date = models.DateTimeField(auto_now=True, verbose_name="дата оплаты")
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="оплаченный курс", **NULLEBELL
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="оплаченный урок", **NULLEBELL
    )
    payment_sum = models.PositiveIntegerField(verbose_name="сумма платежа")
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHOD_CHOICES,
        default="card",
        verbose_name="способ оплаты",
    )
    payment_link = models.URLField(
        max_length=400, verbose_name="ссылка на оплату", **NULLEBELL
    )
    payment_id = models.CharField(
        max_length=255, verbose_name="идентификатор платежа", **NULLEBELL
    )

    def __str__(self):
        return (
            f"{self.user}: {self.payments_date}, {self.payment_sum}, {self.payment_id}"
            f"{self.paid_course if self.paid_course else self.paid_lesson}"
        )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ["-payments_date"]
