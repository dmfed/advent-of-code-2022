import sys

def readfile(filename: str) -> list:
    out = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            out.append(line.strip())
    return out


def solve(data: list):
    return find_data_start(data[0])


def solve2(data: list):
    return find_message_start(data[0])


def find_data_start(line: str) -> int:
    idx = 0
    for i in range(0, len(line)-4):
        temp = set(line[i:i+4])
        if len(temp) == 4:
            idx = i+4
            break
    return idx

def find_message_start(line: str) -> int:
    idx = 0
    for i in range(0, len(line)-4):
        data_start = set(line[i:i+4])
        message_start = set(line[i+4:i+4+14])
        if len(data_start) == 4 and len(message_start) == 14:
            idx = i+4+14
            break
    return idx

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('supply filename')
        sys.exit()

    data = readfile(sys.argv[1])

    n = solve(data) # task 1
    print(n)


    n = solve2(data) # task 2
    print(n)


