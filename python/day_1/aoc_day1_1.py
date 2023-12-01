from rich import print
from utils.utils import get_data, exract_digits, first_last


def main() -> None:
    input_data = get_data("./../../data")
    extracted = exract_digits(input_data)

    print(sum(first_last(extracted)))


if __name__ == "__main__":
    main()
