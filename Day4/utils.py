def nums_from_str(line):
    return [int(x) for x in line.split(' ') if x != '']


def get_data(fname):
    with open(fname) as f:
        data = f.readlines()
    for i, line in enumerate(data):
        id1, id2 = line.index(':'), line.index('|')     # get the positions of : and |
        winning = nums_from_str(data[i][id1+1:id2].strip())
        players = nums_from_str(data[i][id2+1:].strip())
        data[i] = [winning, players]
    return data
