# Generated by Django 5.0 on 2024-03-29 04:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0002_alter_courseprice_options_alter_lessonprice_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="courseprice",
            options={
                "verbose_name": "Цена курса",
                "verbose_name_plural": "Цены курсов",
            },
        ),
        migrations.AlterModelOptions(
            name="lessonprice",
            options={
                "verbose_name": "Цена урока",
                "verbose_name_plural": "Цены уроков",
            },
        ),
    ]
