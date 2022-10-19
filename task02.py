# Разработайте программу, которая проверяет, что все цифры заданного
# натурального числа различны

def same_digits(number):
    digit_1 = 0
    digit_2 = 0
    while number > 0:
        digit_1 = number % 10
        number = number // 10
        if number != 0:
            digit_2 = number % 10
            if digit_1 != digit_2:
                number = number = number // 10
        else:
            break

    return True if digit_1 != digit_2 else False


def main():
    number = int(input("Input your number: "))

    result = same_digits(number)

    msg = f"All digits of number {number} are different - it is {result}."
    print(msg)


main()
