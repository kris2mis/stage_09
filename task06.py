# Начальный вклад в банке равен 1000 руб. При ежемесячной капитализации
# через каждый месяц размер вклада увеличивается на P процентов от имею-
# щейся суммы (P – вещественное число, которое должно удовлетворять нера-
# венству 0 < P < 25). По данному P определить, через сколько месяцев размер
# вклада превысит 2000 руб., и вывести найденное количество месяцев K (целое
# число) и итоговый размер вклада S (вещественное число).

def calc_month(p):
    start_capital = 1000
    k = 1
    s = 1
    while start_capital < 2000:
        s = start_capital + start_capital * (p / 100) * k
        if s < 2000 and 0 < p < 25:
            k += 1
        else:
            break

    return k


def main():
    p = float(input("Input the percent: "))
    start_capital = 1000

    month = calc_month(p)
    s = start_capital + start_capital * (p / 100) * month

    msg = f"Finish capilal is {s}.\nCount of month: {month} "

    print(msg)


main()
