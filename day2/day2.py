import sys

ROCK = 1 
PAPER = 2
SCI = 3 

FIGURES = [ROCK, PAPER, SCI]

IDX_FIG = { 'A': 0, 'X': 0, 'B': 1, 'Y': 1, 'C': 2, 'Z': 2} 

RES_LOOSE = 0
RES_DRAW = 3
RES_WIN = 6

IDX_RES = {'X': RES_LOOSE, 'Y': RES_DRAW, 'Z': RES_WIN}

def readfile(filename: str) -> list:
    out = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            out.append(line.strip())
    return out


def solve(inp: list) -> int:
    result = 0  
    for l in inp:
        opp, me = l.split()
        result += FIGURES[IDX_FIG[me]] + outcome(opp, me) 
    return result


def solve2(inp: list) -> int:
    result = 0
    for l in inp:
        opp, want = l.split()
        result += IDX_RES[want] + winning_move(opp, want)
    return result


def outcome(opp, me) -> int:
    if IDX_FIG[opp] == IDX_FIG[me]:
        return RES_DRAW
    elif FIGURES[IDX_FIG[me] - 1] == FIGURES[IDX_FIG[opp]]:
        return RES_WIN
    return RES_LOOSE


def winning_move(opp: str, need: str) -> int:
    if IDX_RES[need] == RES_DRAW:
        return FIGURES[IDX_FIG[opp]]
    elif IDX_RES[need] == RES_WIN:
        return FIGURES[(IDX_FIG[opp] + 1) % len(FIGURES)]
    else:
        return FIGURES[IDX_FIG[opp] - 1]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('supply filename')
        sys.exit()

    data = readfile(sys.argv[1])

    n = solve(data) # task 1
    print(n)
    n = solve2(data) # task 2
    print(n)




