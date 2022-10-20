# Написать программу, которая подсчитывает количество только чётных (или
# нечётных) цифр заданного натурального числа

def count_even_digits(number):
    number *= -1 if number < 0 else 1
    count = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit % 2 == 0:
            count += 1
        else:
            count += 0

    return count


def main():
    number = int(input("Input your number: "))

    result = count_even_digits(number)

    msg = f"Count of even digits of {number}  is {result}."

    print(msg)


main()
