def get_data(filename: str) -> list:
    data = []

    with open(filename, "r") as file:
        data = file.readlines()

    return data


def replace_string_digits(data: list) -> list:
    string_digits = {
        "one": "o1e",
        "two": "t2o",
        "three": "th3ee",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "se7en",
        "eight": "ei8t",
        "nine": "n9e",
    }

    for i in range(len(data)):
        for key, value in string_digits.items():
            data[i] = data[i].replace(key, value)

    return data


def exract_digits(data: list) -> list:
    extracted = []
    for x in range(len(data)):
        extracted.append("".join([str(i) for char in data[x] for i in range(10) if char == str(i)]))

    return extracted


def first_last(data: list) -> list:
    num_array = []

    for num in data:
        if len(num) == 1:
            temp_num = num
            temp_num += num
            num_array.append(int(temp_num))
        elif len(num) > 2:
            num_one = num[0]
            num_two = num[len(num) - 1]

            temp_num = num_one + num_two
            num_array.append(int(temp_num))
        else:
            num_array.append(int(num))

    return num_array
