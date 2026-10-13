from django.db import models

class CorporateClient(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компании')
    inn = models.CharField(max_length=12, unique=True, verbose_name='ИНН', help_text='10 цифр для юридических лиц / 12 цифр для ИП')
    industry = models.CharField(max_length=100, verbose_name='Отрасль')
    registration_date = models.DateField(verbose_name='Дата регистрации компании')
    is_active = models.BooleanField(default=True, verbose_name='Статус клиента')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.name} - {self.inn}'

    class Meta:
        verbose_name = 'Корпоративный клиент'
        verbose_name_plural = 'Корпоративные клиенты'
        ordering = ['-created_at']

