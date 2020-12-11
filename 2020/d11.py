def part1(seats):
    dirs = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]
    temp = [i[:] for i in seats]
    while True:
        is_l = []
        js_l = []
        is_h = []
        js_h = []
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == 'L':
                    count = 0
                    for d in dirs:
                        if i+d[0] < 0 or i+d[0] >= len(seats):
                            continue
                        if j+d[1] < 0 or j+d[1] >= len(seats[0]):
                            continue
                        if seats[i+d[0]][j+d[1]] == '#':
                            count = 1
                            break
                    if not count:
                        is_l.append(i)
                        js_l.append(j)
                elif seats[i][j] == '#':
                    count = 0
                    for d in dirs:
                        if i+d[0] < 0 or i+d[0] >= len(seats):
                            continue
                        if j+d[1] < 0 or j+d[1] >= len(seats[0]):
                            continue
                        if seats[i+d[0]][j+d[1]] == '#':
                            count += 1
                    if count >= 4:
                        is_h.append(i)
                        js_h.append(j)
        for k in range(len(is_l)):
            seats[is_l[k]][js_l[k]] = '#'
        for k in range(len(is_h)):
            seats[is_h[k]][js_h[k]] = 'L'
        if temp == seats:
            break
        temp = [i[:] for i in seats]
    count = 0
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == '#':
                count += 1
    return count


def part2(seats):
    dirs = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]
    temp = [i[:] for i in seats]
    while True:
        is_l = []
        js_l = []
        is_h = []
        js_h = []
        for r in range(len(seats)):
            for c in range(len(seats[0])):
                if seats[r][c] == 'L':
                    count = 0
                    for d in dirs:
                        i, j = r, c
                        while not (i+d[0] < 0 or i+d[0] >= len(seats)) and \
                            not (j+d[1] < 0 or j+d[1] >= len(seats[0])):
                            i += d[0]
                            j += d[1]
                            if seats[i][j] == '#':
                                count = 1
                                break
                            elif seats[i][j] == 'L':
                                break
                        if count:
                            break
                    if not count:
                        is_l.append(r)
                        js_l.append(c)
                elif seats[r][c] == '#':
                    count = 0
                    for d in dirs:
                        i, j = r, c
                        while not (i+d[0] < 0 or i+d[0] >= len(seats)) and \
                            not (j+d[1] < 0 or j+d[1] >= len(seats[0])):
                            i += d[0]
                            j += d[1]
                            if seats[i][j] == '#':
                                count += 1
                                break
                            elif seats[i][j] == 'L':
                                break
                        if count >= 5:
                            break
                    if count >= 5:
                        is_h.append(r)
                        js_h.append(c)
        for k in range(len(is_l)):
            seats[is_l[k]][js_l[k]] = '#'
        for k in range(len(is_h)):
            seats[is_h[k]][js_h[k]] = 'L'
        if temp == seats:
            break
        temp = [i[:] for i in seats]
    count = 0
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == '#':
                count += 1
    return count


def solution(file):
    count = 0
    grid = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            grid.append(list(line))
    return part2(grid)


if __name__ == '__main__':
    result = solution('input/d11.txt')
    print(result)
