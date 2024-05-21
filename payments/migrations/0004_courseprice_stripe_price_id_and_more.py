# Generated by Django 5.0 on 2024-03-30 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0003_alter_courseprice_options_alter_lessonprice_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="courseprice",
            name="stripe_price_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="courseprice",
            name="stripe_product_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]