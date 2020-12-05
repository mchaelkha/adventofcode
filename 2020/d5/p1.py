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
    max_id = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            row = find_row(line[:7])
            col = find_col(line[7:])
            max_id = max(row * 8 + col, max_id)
    return max_id


if __name__ == '__main__':
    result = solution('d5.txt')
    print(result)
