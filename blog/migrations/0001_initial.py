# Generated by Django 5.1.3 on 2024-12-20 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите заголовок блога",
                        max_length=150,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="Введите содержимое блога", verbose_name="Содержимое"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрзите фото продукта",
                        null=True,
                        upload_to="blog/image",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Введите дату создания",
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "publication",
                    models.BooleanField(default=True, verbose_name="Публикация"),
                ),
                (
                    "number_views",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Укажите кол-во просмотров",
                        verbose_name="Кол-во просмотров",
                    ),
                ),
            ],
            options={
                "verbose_name": "блог",
                "verbose_name_plural": "блоги",
            },
        ),
    ]