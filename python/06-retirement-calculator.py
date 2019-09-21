from datetime import date


def get_int_input(message: str) -> int:
    while True:
        try:
            return int(input(message + " "))
        except ValueError:
            print("Could not interpret your input as a number. Please try again.")


def get_age() -> int:
    return get_int_input("What is your current age?")


def get_retirement_age() -> int:
    return get_int_input("At what age would you like to retire?")


def format_report(years_left: int, current_year: int, retirement_year: int) -> str:
    if years_left < 0:
        return "You can already retire."
    return f"""\
You have {years_left} {"year" if years_left == 1 else "years"} left until you can retire.
It's {current_year}, so you can retire in {retirement_year}."""


def main() -> None:
    age = get_age()
    retire_at = get_retirement_age()
    years_left = retire_at - age

    current_year = date.today().year
    retirement_year = current_year + years_left

    print(format_report(years_left, current_year, retirement_year))


if __name__ == "__main__":
    main()
