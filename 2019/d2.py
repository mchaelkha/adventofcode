def process(csv):
    # csv[1] = 12
    # csv[2] = 2
    step = 4
    # opcodes = [1, 2, 99]
    for i in range(0, len(csv), step):
        op = csv[i]
        a = csv[csv[i + 1]]
        b = csv[csv[i + 2]]
        if op == 99:
            return csv[0]
        elif op == 1:
            csv[csv[i + 3]] = a + b
        elif op == 2:
            csv[csv[i + 3]] = a * b
    return csv[0]


def solution(file):
    csv = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            csv = [int(i) for i in line.split(',')]
    for i in range(100):
        for j in range(100):
            # csv[:] = csv.copy()
            temp = csv[:]
            csv[1] = i
            csv[2] = j
            if process(csv) == 19690720:
                return 100 * i + j
            csv = temp


if __name__ == '__main__':
    result = solution('input/d2.txt')
    print(result)
