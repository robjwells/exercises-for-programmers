from operator import add, sub, mul, truediv


def main():
    while True:
        first = prompt_for_number("first")
        second = prompt_for_number("second")
        operations = [("+", add), ("-", sub), ("*", mul)]

        for symbol, operator in operations:
            print(f"{first} {symbol} {second} = {operator(first, second)}")

        if second != 0:
            div_result = truediv(first, second)
            if div_result.is_integer():
                div_result = int(div_result)
            print(f"{first} / {second} = {div_result}")
        else:
            print(f"{first} / {second} is not defined")


def prompt_for_number(which):
    while True:
        num = input(f"What is the {which} number? ")
        try:
            num = int(num)
            return num
        except ValueError:
            print(f"Could not parse {num} as a number. Please try again")
            continue


if __name__ == "__main__":
    main()
