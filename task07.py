# Разработайте программу, которая с использованием эффективного алгоритма
# находит максимальную цифру заданного натурального числа. К примеру, в
# числе 18273645 максимальная цифра восемь, а в числе 777 – семь

def find_max_digit(number):
    max_digit = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit > max_digit:
            max_digit = digit
    return max_digit


def main():
    number = int(input("Input your number: "))
    result = find_max_digit(number)

    msg = f"Max digit of {number} is {result}."

    print(msg)


main()
