import sys


def readfile(filename: str) -> list:
    lines = list()
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def lines_to_ints(lines: list) -> list:
    l = list()
    curr = 0
    for line in lines:
        if line != '':
            curr += int(line)
        else:
            l.append(curr)
            curr = 0
    l.append(curr)
    return l 

if __name__ == '__main__':
    inp = readfile(sys.argv[1])
    numbers = lines_to_ints(inp)
    print(max(numbers)) # first task
    print(sum(sorted(numbers, reverse=True)[:3])) # second task
