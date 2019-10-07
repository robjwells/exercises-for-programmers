def prompt_how_many(thing: str) -> int:
    while True:
        try:
            answer = input(f"How many {thing}? ")
            parsed = int(answer)
            if parsed < 1:
                print(f"You must have more than 0 {thing}, please try again.")
                continue
            return parsed
        except ValueError:
            print(f"Could not intrept {answer} as an integer, please try again.")


def report_people_and_pizzas(people: int, pizzas: int) -> None:
    print(f"{people} people with {pizzas} pizzas.")


def report_slices(per_person: int, leftover: int) -> None:
    per_person_noun = "slice" if per_person == 1 else "slices"
    leftover_noun = "slice" if leftover == 1 else "slices"
    print(f"Each person with {per_person} {per_person_noun} of pizza.")
    print(f"There are {leftover} leftover {leftover_noun}.")


def main() -> None:
    people = prompt_how_many("people")
    pizzas = prompt_how_many("pizzas")
    slices = prompt_how_many("slices per pizza")
    print()
    report_people_and_pizzas(people, pizzas)

    total_slices = pizzas * slices
    slices_per_person, leftover_slices = divmod(total_slices, people)
    report_slices(slices_per_person, leftover_slices)


if __name__ == "__main__":
    main()
