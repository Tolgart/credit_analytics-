from django.db import models


class IndustryChoices(models.TextChoices):
    TRADE_WHOLESALE = 'TRADE_WHOLESALE', 'Торговля оптовая'
    TRADE_RETAIL = 'TRADE_RETAIL', 'Торговля розничная'
    CONSTRUCTION = 'CONSTRUCTION', 'Строительство'
    MANUFACTURING = 'MANUFACTURING', 'Промышленность / Производство'
    TRANSPORT_LOGISTICS = 'TRANSPORT_LOGISTICS', 'Транспорт и логистика'
    AGRICULTURE = 'AGRICULTURE', 'Сельское хозяйство'
    REAL_ESTATE = 'REAL_ESTATE', 'Недвижимость'
    RENTAL_LEASING = 'RENTAL_LEASING', 'Аренда и лизинг'
    FINANCE_INSURANCE = 'FINANCE_INSURANCE', 'Финансы и страхование'
    IT_TELECOM = 'IT_TELECOM', 'IT и телекоммуникации'
    MINING = 'MINING', 'Добывающая промышленность'
    ENERGY = 'ENERGY', 'Энергетика'
    HOSPITALITY = 'HOSPITALITY', 'Гостиницы и рестораны'
    PROFESSIONAL_SERVICES = 'PROFESSIONAL_SERVICES', 'Профессиональные услуги'
    HEALTHCARE = 'HEALTHCARE', 'Здравоохранение'
    OTHER = 'OTHER', 'Прочее'


class CorporateClient(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компании')
    inn = models.CharField(max_length=12, unique=True, verbose_name='ИНН', help_text='10 цифр для юридических лиц / 12 цифр для ИП')
    industry = models.CharField(max_length=100, choices=IndustryChoices, verbose_name='Отрасль')
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

