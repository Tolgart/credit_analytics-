from clients.models import FinancialStatement


def calculate_debt_to_equity(net_debt, equity):
    """
    Функция для расчёта коэффициента Долг/Капитал
    """
    return net_debt / equity if equity != 0 else 0


def calculate_ebitda_margin(ebitda, revenue):
    """
    Функция для расчёта показателя "Рентабельность по EBITDA"
    """
    return ebitda / revenue * 100


def calculate_roe(ebitda, equity):
    """
    Функция для расчёта показателя "Рентабельность капитала"
    """
    return ebitda / equity * 100


def get_client_financial_summary(financial_statement):
    """
    Функция для расчёта всех финансовых коэффициентов за конкретный период и передачи их в виде
    словаря
    """
    if not financial_statement:
        return None

    net_debt = financial_statement.net_debt
    equity = financial_statement.equity
    ebitda = financial_statement.ebitda
    revenue = financial_statement.revenue

    return {
        'debt_to_equity': calculate_debt_to_equity(net_debt, equity),
        'ebitda_margin': calculate_ebitda_margin(ebitda, revenue),
        'roe': calculate_roe(ebitda, equity),
    }


def get_periods_for_analysis(client):
    if not client:
        return None

    # Выгружаем последний период отчетности клиента
    current_period = client.financial_statements.first()

    if current_period:
        quarter = current_period.period.split()[0]
        year = current_period.period.split()[1]

        if quarter != 'Q4':
            try:
                full_last_year = client.financial_statements.get(period=' '.join(('Q4', str(int(year)-1))))
            except FinancialStatement.DoesNotExist:
                full_last_year = None

            try:
                same_period_last_year = client.financial_statements.get(period=' '.join((quarter, str(int(year)-1))))
            except FinancialStatement.DoesNotExist:
                same_period_last_year = None

        else:
            try:
                full_last_year = client.financial_statements.get(period=' '.join(('Q4', str(int(year)-1))))
            except FinancialStatement.DoesNotExist:
                full_last_year = None

            same_period_last_year = None

    else:
        current_period = None
        full_last_year = None
        same_period_last_year = None

    return {'current_period': current_period,
            'full_last_year': full_last_year,
            'same_period_last_year': same_period_last_year,
            }
