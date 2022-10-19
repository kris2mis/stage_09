# Начальный вклад в банке равен 1000 руб. При ежемесячной капитализации
# через каждый месяц размер вклада увеличивается на P процентов от имею-
# щейся суммы (P – вещественное число, которое должно удовлетворять нера-
# венству 0 < P < 25). По данному P определить, через сколько месяцев размер
# вклада превысит 2000 руб., и вывести найденное количество месяцев K (целое
# число) и итоговый размер вклада S (вещественное число).

def calc_finish_capital(p):
    start_capital = 1000
    capital_limit = 2000
    k = 1
    while start_capital < 2000:
        S = start_capital * (1 + p / 100)
        k += 1
        month = int(S // 30)
        break
    return S, k, month


def main():
    p = float(input("Input the percent: "))

    finish_capilal = calc_finish_capital(p)
    k = calc_finish_capital(p)
    month = calc_finish_capital(p)

    msg = f"Finish capilal is {finish_capilal}. " \
          f"Count of month - {k} " \
          f"The summa will be 2000 in {month} month."

    print(msg)


main()
