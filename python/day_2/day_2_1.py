from rich import print

with open("./data/puzzle_input.txt", "r") as file:
    games = file.readlines()

game_data = []
for game_str in games:
    game_id, subsets_str = game_str.split(":")
    subsets = subsets_str.split(";")

    parsed_subsets = [subset.strip().split(", ") for subset in subsets]
    game_data.append((game_id, parsed_subsets))


red_cubes = 12
green_cubes = 13
blue_cubes = 14

possible_games = []
for game_id, subsets in game_data:
    failed_game = False
    for subset in subsets:
        total_counts = {"red": 0, "green": 0, "blue": 0}
        for cube in subset:
            count, color = cube.split()
            total_counts[color] += int(count)
        if total_counts["red"] > red_cubes or total_counts["green"] > green_cubes or total_counts["blue"] > blue_cubes:
            failed_game = True

    if not failed_game:
        possible_games.append(int(game_id.split()[1]))


print(sum(possible_games))
