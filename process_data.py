""" Аналіз балансу
"""

# Підключити функції з модуля 'data_service'
from data_service import get_balance, get_dovidnik

# Структура аналізу балансу вихідних даних
balancee = {
    'balance_name'   : '',              # ім'я балансу
    'pokazniky'     : 0,                # показники
    'pochatok'      : 0.0,              # сума на початок року
    'summa1'        : 0.0,              # сума
    'summa2'        : 0.0,              # сума
    'summa3'        : 0.0,              # сума
    'kinets'        : 0.0,              # темп росту на кінець року
    'temp1'         : 0.0,              # темп росту
    'temp2'         : 0.0,              # темп росту
    'temp3'         : 0.0,              # темп росту
    'temp4'         : 0.0,              # темп росту
}


balances = get_balance()
dovidniks = get_dovidnik()

def balance_means():
    """ Формування аналізу балансу
    """

    def get_dovidnik_name(dovidnik_code):
        """ Повертає назву балансу по його коду
        Args:
            dovidnik_name ([type]): код балансу
        Returns:
            [type]: назва балансу
        """

        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_code:
                return dovidnik[1]

        return "*** Код балансу не знайдений"

    # Накопичувач аналізу балансу
    balance_list = []

    for balance in balances:

        # Створити копію шаблона
        balancee_tmp = balancee.copy()

        balancee_tmp['pokazniky'] = get_dovidnik_name(balance[0])
        balancee_tmp['balance_name'] = balance[1]
        balancee_tmp['pochatok'] = balance[2]
        balancee_tmp['summa1'] = balance[3] 
        balancee_tmp['summa2'] = balance[4]
        balancee_tmp['summa3'] = balance[5]
        balancee_tmp['kinets'] = balance[6] 
        balancee_tmp['temp1'] = float(balancee_tmp['summa1']) / float(balancee_tmp['pochatok']) * 100
        balancee_tmp['temp2'] = float(balancee_tmp['summa2']) / float(balancee_tmp['pochatok']) * 100
        balancee_tmp['temp3'] = float(balancee_tmp['summa3']) / float(balancee_tmp['pochatok']) * 100
        balancee_tmp['temp4'] = float(balancee_tmp['kinets']) / float(balancee_tmp['pochatok']) * 100

        balance_list.append(balancee_tmp)

    return balance_list

result = balance_means()

for r in result:
    print(r)