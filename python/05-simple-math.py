from operator import add, sub, mul, truediv


def main():
    operations = [("+", add), ("-", sub), ("*", mul)]
    template = "{0} {1} {2} = {3}"
    while True:
        first = prompt_for_number("first")
        second = prompt_for_number("second")

        for symbol, operator in operations:
            print(template.format(first, symbol, second, operator(first, second)))

        if second != 0:
            div_result = truediv(first, second)
            if div_result.is_integer():
                div_result = int(div_result)
            print(template.format(first, "/", second, div_result))
        else:
            print(f"{first} / 0 is not defined")


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
