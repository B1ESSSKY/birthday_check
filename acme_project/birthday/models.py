from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from .validators import real_age

User = get_user_model()


class Tag(models.Model):
    tag = models.CharField('Тэг', max_length=20)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.tag


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия',
        max_length=20,
        blank=True,
        help_text='Необязательное поле',
        )
    birthday = models.DateField('День рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthday_images/', blank=True)
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text='Удерживайте "Ctrl" для выбора нескольких тегов',
    )

    class Meta:
        verbose_name = 'День рождения'
        verbose_name_plural = 'Дни рождения'
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

    def get_absolute_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Congratulations(models.Model):
    text = models.TextField('Текст поздравления')
    birthday = models.ForeignKey(
        Birthday,
        verbose_name='День рождения',
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(
        User,
        verbose_name='Автор записи',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Поздравление'
        verbose_name_plural = 'Поздравления'
        ordering = ('created_at',)
