def part1(mass):
    return mass // 3 - 2


def part2(mass):
    mass = part1(mass)
    total = 0
    while mass > 0:
        total += mass
        mass = part1(mass)
    return total


def solution(file):
    count = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            temp = part2(int(line))
            count += temp
    return count


if __name__ == '__main__':
    result = solution('input/d1.txt')
    print(result)
