# Generated by Django 3.2.16 on 2024-12-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0004_auto_20241203_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='image',
            field=models.ImageField(blank=True, upload_to='birthday_images/', verbose_name='Фото'),
        ),
    ]
