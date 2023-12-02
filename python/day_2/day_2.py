from utils.utils import parse_data, part_one_solve, part_two_solve
from rich import print

with open("./data/puzzle_input.txt", "r") as file:
    games = file.readlines()


def part_one() -> None:
    parsed_data = parse_data(games)

    print(part_one_solve(parsed_data))
    print(part_two_solve(parsed_data))


if __name__ == "__main__":
    part_one()
