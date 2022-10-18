# Разработайте программу, которая проверяет, что все цифры заданного натурального числа одинаковы

def same_digits(number):
    digit_1 = 0
    digit_2 = 0
    result = False
    while number > 0:
        digit_1 = number % 10
        number = number // 10
        while number > 0:
            digit_2 = number % 10
            number = number // 10
            if digit_1 == digit_2:
                result = True
                # number = number // 10
    return result

    # if digit_1 > 0:
    #     number = number // 10

def main():
    number = int(input("Input your number: "))

    result = same_digits(number)

    msg = f"All digits of number {number} are the same - it is {result}."
    print(msg)


main()
