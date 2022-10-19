# # Разработайте программу, которая проверяет, что цифры заданного числа образуют
# # возрастающую (убывающую) последовательность (к примеру, число 1357 удовлетворяет условию,
# # т.к. его цифры соответствуют следующему неравенству: 1 < 3 < 5 < 7, т.е. идут в порядке возрастания;
# # число 98765 также удовлетворяет условию, т.к. его цифры соответствуют следующему неравенству 9
# # > 8 > 7 > 6 > 5; а вот числа 192837, 777, 19283746 – не удовлетворяют условию)
#
# def check_sequence(number):
#     while number > 0:
#         digit_1 = number % 10
#         number = number // 10
#         if number != 0:
#             digit_2 = number % 10
#             if digit_1 > digit_2:
#                 number = number // 10
#                 result = "+"
#             elif digit_1 < digit_2:
#                 number = number // 10
#                 result = "-"
#
#             else:
#                 result = False
#
#
#     return result
#
#
# def main():
#     number = int(input("Input your number: "))
#
#     result = check_sequence(number)
#
#     msg = f"Number {number} are in order- it is {result}."
#     print(msg)
#
#
# main()

# Разработайте программу, которая проверяет, что цифры заданного числа образуют
# возрастающую (убывающую) последовательность (к примеру, число 1357 удовлетворяет условию,
# т.к. его цифры соответствуют следующему неравенству: 1 < 3 < 5 < 7, т.е. идут в порядке возрастания;
# число 98765 также удовлетворяет условию, т.к. его цифры соответствуют следующему неравенству 9
# > 8 > 7 > 6 > 5; а вот числа 192837, 777, 19283746 – не удовлетворяют условию)

def check_sequence(number):
    while number > 0:
        digit_1 = number % 10
        number = number // 10
        if number != 0:
            digit_2 = number % 10
            if digit_1 != digit_2:
                if digit_1 > digit_2:
                    number = number // 10
                    result = "+"
                elif digit_1 < digit_2:
                    number = number // 10
                    result = "-"
            else:
                result = False

    return result


def main():
    number = int(input("Input your number: "))

    result = check_sequence(number)

    msg = f"The order of {number} is {result}."
    print(msg)


main()
