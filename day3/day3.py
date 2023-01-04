import sys

OFFSET_LOWER = ord('a') - 1
OFFSET_UPPER = ord('A') - 27

def readfile(filename: str) -> list:
    out = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            out.append(line.strip())
    return out


def solve(data: list):
    result = 0
    for line in data:
        n = find_common(split_line(line))
        m = get_value(n)
        result += m
    return result


def solve2(data: list):
    result = 0
    for i in range(0, len(data), 3):
        a, b, c = tuple(data[i:i+3])
        result += get_value(find_common_in_three(a, b, c))
    return result


def split_line(line: str):
    return line[:len(line)//2], line[len(line)//2:]


def find_common(inp: tuple) -> str:
    return ''.join(set(list(inp[0])) & set(list(inp[1])))


def get_value(s: str) -> int:
    if s.isupper():
        return ord(s) - OFFSET_UPPER
    else:
        return ord(s) - OFFSET_LOWER


def find_common_in_three(a, b, c):
    return ''.join(set(list(a)) & set(list(b)) & set(list(c)))

    


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('supply filename')
        sys.exit()

    data = readfile(sys.argv[1])

    n = solve(data) # task 1
    print(n)
    n = solve2(data) # task2
    print(n)




