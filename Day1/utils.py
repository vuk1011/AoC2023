import utils


def get_input(file_name):
    with open(file_name) as f:
        data = f.readlines()
    data = [line[:-1] for line in data]
    return data


def print_list(lst):
    [print(row) for row in lst]


def get_num_from_digits(digits: list[int]) -> int:
    return digits[0] * 10 + digits[-1]


def get_num_1(line: str) -> int:
    digits = [int(char) for char in line if char.isnumeric()]
    return get_num_from_digits(digits)


replacements = {"one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9"}


def get_first_digit_index(line: str) -> int:
    i = -1
    for j, char in enumerate(line):
        if char.isnumeric():
            i = j
            break
    return i


def get_last_digit_index(line: str) -> int:
    for i in range(len(line) - 1, -1, -1):
        if line[i].isnumeric():
            return i
    return -1


def get_first_word_index(line: str) -> int:
    positions = []
    for value in replacements:
        try:
            positions.append(line.index(value))
        except Exception:
            pass
    if len(positions) == 0:
        return -1
    else:
        return min(positions)






def get_num_2(line: str) -> int:
    pass