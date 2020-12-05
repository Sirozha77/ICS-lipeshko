""" Головний модуль задачі
- Виводить розрахункову табліцю на екран та в файл
- Виводить первинні данні на екран
"""

import os
from process_data import balance_means
from data_service import show_dovidniks, show_balances, get_dovidnik, get_balance

MAIN_MENU = \
""" 
~~~~~~~~   Аналіз динаміки оборотних коштів та оборотного капіталу підприємства    ~~~~~~~~
1 - Вивід таблиці динаміки оборотних коштів та оборотного капіталу підприємства
2 - Запис таблиці динаміки оборотних коштів та оборотного капіталу підприємства в файл
3 - Вивід списка балансу
4 - Вивід списка довідника показників балансу
0 - Завершення роботи
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

TITLE = " АНАЛІЗ ДИНАМІКИ ОБОРОТНИХ КОШТІВ ТА ОБОРОТНОГО КАПІТАЛУ ПІДПРИЄМСТВА"

HEADER = \
"""
=====================================================================================================================================
|  Назва підрозділу |   Показник  |  На початок року  |  На початок 2 кв   |  На початок 3 кв |  На початок 4 кв  |  На кінець року |
|      балансу      |             |                   |   сума, | Темп     |   сума, | Темп   |   сума, | Темп    |   сума, | Темп  |
|                   |             |                   |   т.грн | росту    |   т.грн | росту  |   т.грн | росту   |   т.грн | росту |                
=====================================================================================================================================
"""

FOOTER =  \
'''
=============================================================================================================================
'''

STOP_MESSAGE = '\nДля продовження натисніть <Enter> '

def show_balance(balance_list):
    """ Виводить таблицю балансу 
    Args:
        balance_list ([type]): Список балансу
    """
    print(f"\n\n{TITLE:^141}")
    print(HEADER)

    for balance in balance_list:
        print(f"{balance['balance_name']:19}",
              f"{balance['pokazniky']:^13}",
              f"{balance['pochatok']:^19}",
              f"{balance['summa1']:^9}",
              f"{balance['summa2']:^9}",
              f"{balance['summa3']:^9}",
              f"{balance['kinets']:^9}",
              f"{balance['temp1']:^10}",
              f"{balance['temp2']:^8}",
              f"{balance['temp3']:^9}",
              f"{balance['temp4']:^7}")

    print(FOOTER)

def write_balance(balance_list):
    """ Записує список балансу у текстовий файл
    Args:
        balance_list ([type]): список балансу
    """

    with open('./data/balance.txt', 'w') as balance_file:
        for balance in balance_list:
            line = \
               balance['balance_name'] + ';' +          \
               balance['pokazniky'] + ';' +             \
               str(balance['pochatok']) + ';' +      \
               str(balance['summa1']) + ';' +       \
               str(balance['summa2']) + ';' +    \
               str(balance['summa3']) + ';' +      \
               str(balance['kinets'])  + ';' +      \
               str(balance['temp1']) + ';' +      \
               str(balance['temp2']) + ';' +      \
               str(balance['temp3']) + ';' +      \
               str(balance['temp4']) + '\n'
               
            balance_file.write(line)  
            
    print('\n[INFO]: Файл успішно записано...')     

while True:

    # Виводить головне меню
    os.system('cls')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # Обробка команд користувача
    if command_number == '0':
        print('\n[INFO]: Програма завершила роботу\n')
        exit(0)

    elif command_number == '1':
        balance_list = balance_means()
        show_balance(balance_list)
        input(STOP_MESSAGE)

    elif command_number == '2':
        balance_list = balance_means()
        write_balance(balance_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        balances = get_balance()
        show_balances(balances)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        dovidniks = get_dovidnik()
        show_dovidniks(dovidniks)
        input(STOP_MESSAGE)