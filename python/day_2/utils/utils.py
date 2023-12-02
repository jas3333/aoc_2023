from rich import print
from functools import reduce


def parse_data(data: list) -> list:
    game_data = []

    for string in data:
        game_id, substring = string.split(":")
        substring_sets = substring.split(";")
        parsed_subsets = [subset.strip().split(", ") for subset in substring_sets]

        game_data.append((game_id, parsed_subsets))

    return game_data


def part_one_solve(data: list) -> int:
    RED_CUBES = 12
    GREEN_CUBES = 13
    BLUE_CUBES = 14

    possible_games = []

    for game_id, subsets in data:
        failed_game = False

        for subset in subsets:
            total_counts = {"red": 0, "green": 0, "blue": 0}

            for cube in subset:
                count, color = cube.split()
                total_counts[color] += int(count)

            if (
                total_counts["red"] > RED_CUBES
                or total_counts["green"] > GREEN_CUBES
                or total_counts["blue"] > BLUE_CUBES
            ):
                failed_game = True
        if not failed_game:
            possible_games.append(int(game_id.split()[1]))

    return sum(possible_games)


def part_two_solve(data: list) -> int:
    counts = []
    for _, subsets in data:
        total_counts = {"red": 0, "green": 0, "blue": 0}
        for subset in subsets:
            for cube in subset:
                count, color = cube.split()
                if total_counts[color] < int(count):
                    total_counts[color] = int(count)
        counts.append([total_counts["red"], total_counts["green"], total_counts["blue"]])

    sum_list = [(num[0] * num[1] * num[2]) for num in counts]

    return sum(sum_list)
