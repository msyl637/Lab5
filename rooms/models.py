from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    COMFORT_CHOICES = [
        ('lux', 'люкс'),
        ('semi', 'полулюкс'),
        ('std', 'обычный'),
    ]

    title = models.CharField(max_length=200, unique=True, verbose_name='Название номера')
    text = models.TextField(verbose_name='Описание')
    capacity = models.PositiveIntegerField(default=1, verbose_name='Вместимость (мест)')
    comfort = models.CharField(max_length=10, choices=COMFORT_CHOICES, default='std', verbose_name='Комфортность')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена за место в сутки')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Автор записи')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
        ordering = ['-created_date']

    def __str__(self):
        return self.title
