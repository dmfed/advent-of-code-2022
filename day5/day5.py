import sys, re, copy

'''
                        [Z] [W] [Z]
        [D] [M]         [L] [P] [G]
    [S] [N] [R]         [S] [F] [N]
    [N] [J] [W]     [J] [F] [D] [F]
[N] [H] [G] [J]     [H] [Q] [H] [P]
[V] [J] [T] [F] [H] [Z] [R] [L] [M]
[C] [M] [C] [D] [F] [T] [P] [S] [S]
[S] [Z] [M] [T] [P] [C] [D] [C] [D]
 1   2   3   4   5   6   7   8   9
'''
STACKS = [
        ['S', 'C', 'V', 'N'],
        ['Z', 'M', 'J', 'H', 'N', 'S'],
        ['M', 'C', 'T', 'G', 'J', 'N', 'D'],
        ['T', 'D', 'F', 'J', 'W', 'R', 'M'],
        ['P', 'F', 'H'],
        ['C', 'T', 'Z', 'H', 'J'],
        ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'],
        ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'],
        ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']
        ]

CMD_RE = re.compile(r'move (\d+) from (\d) to (\d)')

def readfile(filename: str) -> list:
    out = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            out.append(line.strip())
    return out


def solve(data: list):
    st = copy.deepcopy(STACKS)
    for line in data:
        howmany, src, dst = parse_command(line)
        apply_command(st, howmany, src, dst)

    result = "".join([l[-1] for l in st])
    return result


def solve2(data: list):
    st = copy.deepcopy(STACKS)
    for line in data:
        howmany, src, dst = parse_command(line)
        apply_command2(st, howmany, src, dst)

    result = "".join([l[-1] for l in st])
    return result


def parse_command(line: str) -> tuple:
    m = CMD_RE.match(line)
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def apply_command(st, howmany, src, dst: int):
    src -= 1
    dst -= 1
    for _ in range(howmany):
        st[dst].append(st[src].pop())


def apply_command2(st, howmany, src, dst: int):
    src -= 1
    dst -= 1
    st[dst].extend(st[src][-howmany:])
    st[src] = st[src][:-howmany]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('supply filename')
        sys.exit()

    data = readfile(sys.argv[1])

    n = solve(data) # task 1
    print(n)

    n = solve2(data) # task 2
    print(n)



