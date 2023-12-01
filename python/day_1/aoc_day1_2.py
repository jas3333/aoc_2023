from rich.console import Console
from rich.table import Table
from rich import print
from utils.utils import get_data, exract_digits, first_last, replace_string_digits


def main() -> None:
    data_path = "./../../data/input_01.txt"
    console = Console()
    table = Table(title="Output")
    table.add_column("Original")
    table.add_column("Replaced")
    table.add_column("Extracted")
    table.add_column("Final Number")

    input_data = get_data(data_path)
    original = get_data(data_path)
    parsed_digits = replace_string_digits(input_data)
    extracted = exract_digits(parsed_digits)
    final_numbers = first_last(extracted)

    for x in range(len(input_data)):
        table.add_row(original[x], parsed_digits[x], extracted[x], str(final_numbers[x]))

    console.print(table)

    print(sum(final_numbers))


if __name__ == "__main__":
    main()
