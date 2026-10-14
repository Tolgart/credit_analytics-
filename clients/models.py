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


class PeriodChoices(models.TextChoices):
    Q1_2024 = 'Q1 2024', '1 квартал 2024 г.'
    Q2_2024 = 'Q2 2024', '2 квартал 2024 г.'
    Q3_2024 = 'Q3 2024', '3 квартал 2024 г.'
    Q4_2024 = 'Q4 2024', '4 квартал 2024 г.'
    Q1_2025 = 'Q1 2025', '1 квартал 2025 г.'
    Q2_2025 = 'Q2 2025', '2 квартал 2025 г.'
    Q3_2025 = 'Q3 2025', '3 квартал 2025 г.'
    Q4_2025 = 'Q4 2025', '4 квартал 2025 г.'
    Q1_2026 = 'Q1 2026', '1 квартал 2026 г.'
    Q2_2026 = 'Q2 2026', '2 квартал 2026 г.'
    Q3_2026 = 'Q3 2026', '3 квартал 2026 г.'
    Q4_2026 = 'Q4 2026', '4 квартал 2026 г.'


class CorporateClient(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компании')
    inn = models.CharField(max_length=12, unique=True, verbose_name='ИНН', help_text='10 цифр для юридических лиц / 12 цифр для ИП')
    industry = models.CharField(max_length=100, choices=IndustryChoices, verbose_name='Отрасль')
    registration_date = models.DateField(verbose_name='Дата регистрации компании')
    is_active = models.BooleanField(default=True, verbose_name='Статус клиента')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.name}/{self.inn}'

    class Meta:
        verbose_name = 'Корпоративный клиент'
        verbose_name_plural = 'Корпоративные клиенты'
        ordering = ['-created_at']


class FinancialStatement(models.Model):
    client = models.ForeignKey('CorporateClient', on_delete=models.CASCADE, related_name='financial_statements')
    period = models.CharField(max_length=20, choices=PeriodChoices, verbose_name='Период отчета')
    revenue = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Выручка')
    ebitda = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='EBITDA')
    net_debt = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Чистый долг')
    equity = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Собственный капитал')
    report_date = models.DateField(verbose_name='Дата отчета')

    class Meta:
        verbose_name = 'Финансовая отчетность'
        verbose_name_plural = 'Финансовая отчетность'
        ordering = ['client', '-report_date']

