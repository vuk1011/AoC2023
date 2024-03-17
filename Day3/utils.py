def get_data(fname):
    with open(fname) as f:
        data = f.readlines()
    data = [[x for x in line if x != '\n'] for line in data]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j].isnumeric():
                data[i][j] = int(data[i][j])
    return data


class Element:
    def __init__(self, pos: tuple[int, int], val):
        self.pos = pos
        self.val = val
        if isinstance(val, int):
            self.type = 'digit'
        elif val == '.':
            self.type = 'dot'
        else:
            self.type = 'symbol'

    def __str__(self):
        return str(self.val)


class Number:
    def __init__(self, digits: list[Element]):
        self.val = int(''.join([str(d.val) for d in digits]))
        self.pos: set[tuple[int, int]] = {d.pos for d in digits}

    def __str__(self):
        return str(self.val)


class Matrix:
    def __init__(self, data: list[list]):
        self.height = len(data)
        self.width = len(data[0])
        self.elements: list[list[Element]] = [[] for row in data]
        for i in range(self.height):
            for j in range(self.width):
                self.elements[i].append(Element((i, j), data[i][j]))

    def get_element_at_pos(self, pos: tuple[int, int]) -> Element:
        return self.elements[pos[0]][pos[1]]

    def get_neighbours_pos(self, pos) -> set[tuple[int, int]]:
        p = set()
        i, j = pos[0], pos[1]
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di != 0 or dj != 0:
                    if 0 <= i + di < self.height and 0 <= j + dj < self.width:
                        el = self.elements[i + di][j + dj]
                        p.add(el.pos)
        return p

    def get_numbers(self) -> list[list[Element]]:
        nums: list[list[Element]] = []
        for i in range(self.height):
            buff: list[Element] = []
            reading = False
            for j in range(self.width):
                curr = self.elements[i][j]
                if curr.type != 'digit':
                    reading = False
                    if buff:
                        nums.append(buff)
                        buff = []
                else:
                    if reading:
                        buff.append(curr)
                    else:
                        buff.append(curr)
                        reading = True
                if j == self.width - 1 and buff:
                    nums.append(buff)
        return nums


def neighbourhood_has_symbol(m: Matrix, ngh: set[tuple[int, int]]) -> bool:
    for pos in ngh:
        tmp = m.get_element_at_pos(pos)
        if tmp.type == 'symbol':
            return True
    return False
