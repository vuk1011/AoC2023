def get_input(file_name):
    with open(file_name) as f:
        data = f.readlines()
    data = [line[:-1] for line in data]

    # Extract game ID
    data = [row.split(":") for row in data]
    for i, row in enumerate(data):
        id = int(row[0].split(" ")[-1])
        data[i][0] = id

    # Extract game turns
    for i, row in enumerate(data):
        data[i][1] = data[i][1].split(";")

    for i, row in enumerate(data):
        row = [data[i][0]]
        for text in data[i][1]:
            row.append(text)
        data[i] = row

    return data


def print_input(data):
    [print(line) for line in data]


def get_turn(text: str) -> dict:
    turn = {"red": 0, "green": 0, "blue": 0}
    text = [x.strip() for x in text.split(",")]  # Like [ '3 blue' , '4 red' ]
    for x in text:
        x = x.split(" ")
        quantity = int(x[0])
        color = x[1]
        turn[color] = quantity
    return turn


bag = {"red": 12, "green": 13, "blue": 14}


def turn_is_possible(turn: dict) -> bool:
    return turn["red"] <= bag["red"] and turn["green"] <= bag["green"] and turn["blue"] <= bag["blue"]


def power_of_set(cubes: dict) -> int:
    return cubes["red"] * cubes["green"] * cubes["blue"]