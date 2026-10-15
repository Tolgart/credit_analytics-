from django import forms
from clients.models import CorporateClient, FinancialStatement
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit, Div, Field
from crispy_bootstrap5.bootstrap5 import FloatingField


class CorporateClientForm(forms.ModelForm):
    class Meta:
        model = CorporateClient
        fields = ['name', 'inn', 'industry', 'registration_date', 'is_active']
        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ООО "Название"'}),
            'inn': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '12'}),
            'industry': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # Настраиваем структуру формы
        self.helper.layout = Layout(
            # Блок 1: Идентификация клиента
            Fieldset(
                '<i class="bi bi-building"></i> Данные компании',
                Row(
                    Column(FloatingField('name'), css_class='col-md-8'),
                    Column(FloatingField('inn'), css_class='col-md-4'),
                ),
            ),
            # Блок 2: Финансовый профиль
            Fieldset(
                '<i class="bi bi-graph-up"></i> Профиль риска',
                Row(
                    Column(Field('industry', css_class='form-select-lg'), css_class='col-md-6'),
                    Column(Field('registration_date'), css_class='col-md-6'),
                ),
            ),
            # Блок 3: Управление доступом
            Div(
                Field('is_active', wrapper_class='form-check form-switch'),
                css_class='mt-4 p-3 bg-light rounded border'
            ),
            # Кнопка действия
            Submit('submit', 'Сохранить клиента', css_class='btn-primary btn-lg w-100 mt-3')
        )

class FinancialStatementForm(forms.ModelForm):
    class Meta:
        model = FinancialStatement
        fields = ['period', 'revenue', 'ebitda', 'net_debt', 'equity', 'report_date']
        widgets = {
            'period': forms.Select(attrs={'class': 'form-select'}),
            'report_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'revenue': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'ebitda': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'net_debt': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'equity': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Fieldset('Период отчетности',
                Row(
                    Column(Field('period', css_class='form-select-lg'), css_class='col-md-6'),
                Column(Field('report_date'), css_class='col-md-6')
                )
            ),
            Fieldset('Финансовые показатели',
                Row(
                    Column(Field('revenue'), css_class='col-md-3'),
                    Column(Field('ebitda'), css_class='col-md-3'),
                    Column(Field('net_debt'), css_class='col-md-3'),
                    Column(Field( 'equity'), css_class='col-md-3')
                )
            ),
            Submit('submit', 'Добавить отчетность', css_class='btn-primary btn-lg w-100 mt-3')
        )