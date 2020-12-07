import sys

def get_points(cur_r, cur_c, coords, dist):
    r, c = coords
    points = set()
    for i in range(1, dist + 1):
        if r:
            points.add((cur_r + i * r, cur_c))
        elif c:
            points.add((cur_r, cur_c + i * c))
    return points


def process(path):
    lengths = path.split(',')
    points = []
    cur_r, cur_c = 0, 0
    lut = {'L': (0, -1), 'R': (0, 1), 'U': (1, 0), 'D': (-1, 0)}
    for l in lengths:
        pt = lut[l[0]]
        points += get_points(cur_r, cur_c, pt, int(l[1:]))
        if pt[0]:
            cur_r += pt[0] * int(l[1:])
        elif pt[1]:
            cur_c += pt[1] * int(l[1:])
    return set(points)


def get_points_dist(cur_r, cur_c, coords, dist, prev):
    r, c = coords
    points = set()
    for i in range(1, dist + 1):
        if r:
            points.add((cur_r + i * r, cur_c, prev + i))
        elif c:
            points.add((cur_r, cur_c + i * c, prev + i))
    return points


def process_dist(path):
    lengths = path.split(',')
    points = []
    cur_r, cur_c = 0, 0
    curr_dist = 0
    lut = {'L': (0, -1), 'R': (0, 1), 'U': (1, 0), 'D': (-1, 0)}
    for l in lengths:
        pt = lut[l[0]]
        points += get_points_dist(cur_r, cur_c, pt, int(l[1:]), curr_dist)
        if pt[0]:
            cur_r += pt[0] * int(l[1:])
        elif pt[1]:
            cur_c += pt[1] * int(l[1:])
        curr_dist += int(l[1:])
    return set(points)


def part1_intersection(paths):
    first_points = process(paths[0])
    second_points = process(paths[1])
    return first_points.intersection(second_points)


def part1(paths):
    inter = part1_intersection(paths)
    man_dist = sys.maxsize
    for i in inter:
        man_dist = min(man_dist, abs(i[0]) + abs(i[1]))
    return man_dist


def part2(paths):
    first_points = process_dist(paths[0])
    second_points = process_dist(paths[1])
    inter = part1_intersection(paths)
    man_dist = sys.maxsize
    for i in inter:
        first_cost = [p[2] for p in first_points if p[0:2] == i][0]
        second_cost = [p[2] for p in second_points if p[0:2] == i][0]
        man_dist = min(man_dist, first_cost + second_cost)
    return man_dist


def solution(file):
    paths = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            paths.append(line)
    return part2(paths)


if __name__ == '__main__':
    result = solution('input/d3.txt')
    # result = solution('test.txt')
    print(result)
