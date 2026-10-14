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