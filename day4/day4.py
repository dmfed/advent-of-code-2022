import sys

def readfile(filename: str) -> list:
    out = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            out.append(line.strip())
    return out


def solve(data: list):
    result = 0
    for line in data:
        p1, p2 = line_to_pairs(line)
        if pairs_contain_each_other(p1, p2):
            result += 1
    return result


def solve2(data: list):
    result = 0
    for line in data:
        p1, p2 = line_to_pairs(line)
        if pairs_overlap(p1, p2):
            result += 1
    return result


def line_to_pairs(line: str) -> tuple:
    first, second = [tuple(int(n) for n in x.split('-')) for x in line.strip().split(',')]
    return first, second


def pairs_contain_each_other(p1, p2: tuple) -> bool:
    return (p1[0] <= p2[0] and p1[1] >= p2[1]) or (p2[0] <= p1[0] and p2[1] >= p1[1])


def pairs_overlap(p1, p2: tuple) -> bool:
    return (p1[0] <= p2[1] and p1[0] >= p2[0]) or (p2[0] <= p1[1] and p2[0] >= p1[0])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('supply filename')
        sys.exit()

    data = readfile(sys.argv[1])

    n = solve(data) # task 1
    print(n)

    n = solve2(data) # task 2
    print(n)




