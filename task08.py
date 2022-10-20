# Разработайте программу, которая проверяет, что все цифры, которые входят в
# заданное натуральное число, являются чётными.

def even_digits(number):
    number *= -1 if number < 0 else 1
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit // 2 == 0:
            result = True
        else:
            result = False

    return result


def main():
    number = int(input("Input your number: "))

    result = even_digits(number)

    msg = f"All digits of number {number} are even - it is {result}."
    print(msg)


main()