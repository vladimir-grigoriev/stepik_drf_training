# Generated by Django 3.1.7 on 2021-03-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20210306_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='items/', verbose_name='Картинка'),
        ),
    ]
