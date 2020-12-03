def solution(file):
    count = 0
    x_max = 0
    x_pos = 0
    with open(file) as f:
        for row in f:
            row = row.strip()
            if not x_max:
                x_max = len(row)
                continue
            x_pos += 3
            if x_pos >= x_max:
                x_pos -= x_max
            if row[x_pos] == '#':
                count += 1
    return count


if __name__ == '__main__':
    result = solution('input1.txt')
    print(result)
