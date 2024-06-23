# Generated by Django 5.0.6 on 2024-06-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="users/avatars", verbose_name="Аватар"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True, max_length=60, null=True, verbose_name="Город"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True, max_length=45, null=True, verbose_name="Телефон"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                help_text="Указите почту",
                max_length=254,
                unique=True,
                verbose_name="Почта",
            ),
        ),
    ]