SQUARE_FEET_TO_SQUARE_METRES_CONSTANT: float = 0.09290204


def prompt_for_feet(dimension: str) -> float:
    while True:
        response = input(f"What is the {dimension} in feet? ")
        try:
            parsed = float(response)
            return parsed
        except ValueError:
            print(f"Could not parse {response} as a number. Please try again.")


def report_dimensions(length: float, width: float) -> None:
    print(f"You entered dimensions of {length} feet by {width} feet.")


def report_area(square_feet: float, square_metres: float) -> None:
    print(
        "The area is",
        f"{square_feet} square feet",
        f"{square_metres} square metres",
        sep="\n",
    )


def sqft_to_sqm(square_feet: float) -> float:
    return square_feet * SQUARE_FEET_TO_SQUARE_METRES_CONSTANT


def main() -> None:
    length_ft = prompt_for_feet(dimension="length")
    width_ft = prompt_for_feet(dimension="width")

    report_dimensions(length_ft, width_ft)

    square_feet = length_ft * width_ft
    square_metres = sqft_to_sqm(square_feet)

    report_area(square_feet, square_metres)


if __name__ == "__main__":
    main()
