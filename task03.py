# сколько раз цифра встречается в заданом числе

def count_digit(number):
    digit = 0
    count = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit == 0:
            count += 1
    return count


def main():
    number = int(input("Input your number: "))

    result = count_digit(number)

    msg = f"{result} times."

    print(msg)


main()
