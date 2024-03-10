# Generated by Django 5.0 on 2024-03-07 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                    models.CharField(max_length=250, verbose_name="название курса"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="описание курса"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="course_images/",
                        verbose_name="превью курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "курс",
                "verbose_name_plural": "курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                    models.CharField(max_length=250, verbose_name="название урока"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="описание урокаа"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="course_images/",
                        verbose_name="превью урока",
                    ),
                ),
                (
                    "video_link",
                    models.URLField(
                        blank=True, null=True, verbose_name="ссылка на видео"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="materials.course",
                        verbose_name="название курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "урок",
                "verbose_name_plural": "уроки",
            },
        ),
    ]