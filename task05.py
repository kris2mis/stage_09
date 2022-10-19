# Разработайте программу, которая проверяет, что заданное натуральное число
# читается одинаково слева направо и справа налево (т.е. является палиндро-
# мом). К примеру, числа 1235321, 112211, 7 и 1221 – удовлетворяют условию, а
# числа 12345321, 1000 и 12 – нет.


def check_palindrome(number):
    number_test = number[::-1]
    if number == number_test:
        result = True
    else:
        result = False
    return result


def main():
    number = str(input("Input your number: "))

    result = check_palindrome(number)

    msg = f"Number {number} is palindrome - it is {result}."
    print(msg)


main()
