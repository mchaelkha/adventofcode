def find_row(boarding):
    min_row = 0
    max_row = 127
    current = 64
    while len(boarding) > 1:
        ch = boarding[0]
        if ch == 'F':
            max_row -= current
        else:
            min_row += current
        boarding = boarding[1:]
        current //= 2
    return min_row if boarding[0] == 'F' else max_row


def find_col(boarding):
    min_col = 0
    max_col = 7
    current = 4
    while len(boarding) > 1:
        ch = boarding[0]
        if ch == 'L':
            max_col -= current
        else:
            min_col += current
        boarding = boarding[1:]
        current //= 2
    return min_col if boarding[0] == 'L' else max_col


def solution(file):
    count = 0
    grid = [[0] * 8 for i in range(128)]
    ids = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            row = find_row(line[:7])
            col = find_col(line[7:])
            grid[row][col] = row * 8 + col
            ids.append(row * 8 + col)
    # part 1
    # return sorted(ids)[-1]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                temp = r * 8 + c
                if (temp - 1) in ids and (temp + 1) in ids:
                    return temp
    return 0


if __name__ == '__main__':
    result = solution('d5.txt')
    print(result)
