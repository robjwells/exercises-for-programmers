from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import ceil, pi
from typing import List

SQFT_PER_GALLON: int = 350


class Room(ABC):
    """Abstract class that represents a room."""

    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError


@dataclass
class RectangularRoom(Room):
    """Rectangular room with width and height measured in feet."""

    width: float
    length: float

    def area(self) -> float:
        return self.width * self.length


@dataclass
class CircularRoom(Room):
    """Circular room with radius measured in feet."""

    radius: float

    def area(self) -> float:
        return pi * self.radius ** 2


def prompt_for_rectangular_room_details() -> RectangularRoom:
    while True:
        try:
            length = float(input("Length of the room in feet: "))
            break
        except ValueError:
            print("Could not interpret your input as a number. Please try again.")
    while True:
        try:
            width = float(input("Width of the room in feet: "))
            break
        except ValueError:
            print("Could not interpret your input as a number. Please try again.")
    return RectangularRoom(length=length, width=width)


def prompt_for_circular_room_details() -> CircularRoom:
    while True:
        try:
            radius = float(input("Radius of the room in feet: "))
            break
        except ValueError:
            print("Could not interpret your input as a number. Please try again.")
    return CircularRoom(radius=radius)


def get_input_from_user() -> List[Room]:
    rooms: List[Room] = []
    while True:
        rect_or_circ = input(
            "Is the room rectangular (r) or circular (c)? Enter d to finish. "
        )
        if rect_or_circ.lower() == "d":
            break
        elif rect_or_circ.lower() in ("r", "rectangular"):
            rooms.append(prompt_for_rectangular_room_details())
        elif rect_or_circ.lower() in ("c", "circular"):
            rooms.append(prompt_for_circular_room_details())
        else:
            print(
                f"Could not interpret {rect_or_circ} as 'rectangular' or 'circular'. "
                "Please try again."
            )
    return rooms


def main() -> None:
    rooms = get_input_from_user()
    total_sqft = sum(r.area() for r in rooms)
    full_gallons_required = int(ceil(total_sqft / SQFT_PER_GALLON))
    print(
        f"You will need to purchase {full_gallons_required} gallons of paint to cover "
        f"{total_sqft:.0f} square feet."
    )


if __name__ == "__main__":
    main()
