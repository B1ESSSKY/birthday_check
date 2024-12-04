# Generated by Django 3.2.16 on 2024-12-04 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('birthday', '0005_birthday_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Congratulations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст поздравления')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор записи')),
                ('birthday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='congratulations', to='birthday.birthday', verbose_name='День рождения')),
            ],
            options={
                'verbose_name': 'Поздравление',
                'verbose_name_plural': 'Поздравления',
                'ordering': ('created_at',),
            },
        ),
    ]
