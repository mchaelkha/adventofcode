def part1(actions):
    x = 0
    y = 0
    deg = 0
    for a in actions:
        if a[0] == 'L':
            deg += a[1]
        elif a[0] == 'R':
            deg -= a[1]
        elif a[0] == 'F':
            deg %= 360
            if deg == 90:
                y += a[1]
            elif deg == 0:
                x += a[1]
            elif deg == 270:
                y -= a[1]
            elif deg == 180:
                x -= a[1]
        elif a[0] == 'N':
            y += a[1]
        elif a[0] == 'E':
            x += a[1]
        elif a[0] == 'S':
            y -= a[1]
        elif a[0] == 'W':
            x -= a[1]
    return abs(x) + abs(y)


def part2(actions):
    x = 0
    y = 0
    wx = 10
    wy = 1
    for a in actions:
        if a[0] == 'L':
            for i in range(a[1]//90):
                wx, wy = -wy, wx
        elif a[0] == 'R':
            for i in range(a[1]//90):
                wx, wy = wy, -wx
        elif a[0] == 'F':
            y += a[1] * wy
            x += a[1] * wx
        elif a[0] == 'N':
            wy += a[1]
        elif a[0] == 'E':
            wx += a[1]
        elif a[0] == 'S':
            wy -= a[1]
        elif a[0] == 'W':
            wx -= a[1]
    return abs(x) + abs(y)


def solution(file):
    actions = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            actions.append([line[0], int(line[1:])])
    print(part1(actions))
    print(part2(actions))


if __name__ == '__main__':
    solution('input/d12.txt')
