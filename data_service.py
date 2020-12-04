""" Модуль для отримання даних про рух основних засобів та вивід їх на екран
"""

def get_balance():
    """ Повертає вміст файла "balance.txt" у вигляді списка
    Returns:
        balance_list - список рядків файла
    """

    with open('./data/balance.txt', encoding="utf8") as balance_file:
        balance_list = balance_file.readlines()

    # Накопичувач руху основних засобів
    balance_drive = []

    for line in balance_list:
        line_list = line.split(';')
        line_list[6] = line_list[6][:-1]  # Видаляє '\n' в кінці
        balance_drive.append(line_list)


    return balance_drive

def show_balances(balances):
    """ Виводить список балансу
    Args:
        balance (list): список балансу

    """

    # Задати інтервал виводу
    balance_code_from = input("З якого кода балансу виводити?")
    balance_code_to = input("По який код балансу виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for balance in balances:
        if balance_code_from <= balance[0] <= balance_code_to:
            print("Код рядка балансу: {:5} Підрозділ балансу: {:28} 1 кв: {:10} 2 кв: {:10} 3 кв: {:10} 4 кв: {:10} На кінець року: {:10} ".format(balance[0], balance[1], balance[2],balance[3], balance[4], balance[5], balance[6]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту балансу нічого не знайдено.")


balances = get_balance()
show_balances(balances)

def get_dovidnik():
    """ Повертає вміст файла "dovidniks.txt" у вигляді списка
    Returns:
        dovidnik_list - список рядків файла
    """

    with open('./data/dovidnik.txt', encoding="utf8") as dovidnik_file:
        dovidnik_list = dovidnik_file.readlines()

    # Накопичувач довідника основних засобів
    dovidnik_drive = []

    for line in dovidnik_list:
        line_list = line.split(';')
        line_list[1] = line_list[1][:-1]
        dovidnik_drive.append(line_list)


    return dovidnik_drive


def show_dovidniks(dovidniks):
    """ Виводить список довідника
    Args:
        dovidniks (list): список товара
    """

    # Задати інтервал виводу
    dovidnik_code_from = input("З якого кода довідника виводити?")
    dovidnik_code_to = input("По який код довідника виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for dovidnik in dovidniks:
        if dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
            print("Код: {:6} План: {:30}".format(dovidnik[0], dovidnik[1]))
            kol_lines += 1
    
    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту довідника нічого не знайдено.")


dovidniks = get_dovidnik()
show_dovidniks(dovidniks)
