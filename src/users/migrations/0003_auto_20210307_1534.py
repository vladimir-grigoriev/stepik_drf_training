# Generated by Django 3.1.7 on 2021-03-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20210307_1527"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="middle_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Отчество"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Телефон"
            ),
        ),
    ]
