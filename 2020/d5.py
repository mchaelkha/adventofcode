def convert_to_bin(line):
    row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(line[7:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col

def solution(file):
    count = 0
    grid = [[0] * 8 for i in range(128)]
    ids = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            ids.append(convert_to_bin(line))
    # part 1
    # return sorted(ids)[-1]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                temp = r * 8 + c
                if temp not in ids and (temp - 1) in ids and (temp + 1) in ids:
                    return temp
    # part 2 sorting trick
    # lines = sorted(ids)
    # print([(t[0], t[1]) for t in zip(lines[:-1], lines[1:]) if t[1]-t[0] != 1])


if __name__ == '__main__':
    result = solution('input/d5.txt')
    print(result)
