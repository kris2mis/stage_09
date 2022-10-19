# сколько раз цифра встречается в заданом числе

DIGIT = 1

def count_digit(number):
    number *= -1 if number < 0 else 1
    digit = DIGIT
    count = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit == DIGIT:
            count += 1
    return count


def main():
    number = int(input("Input your number: "))

    result = count_digit(number)

    msg = f"{result} times."

    print(msg)


main()
