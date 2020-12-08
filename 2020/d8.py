def part1(I):
    stack = []
    stack.append(I[0])
    acc_total = 0
    called = set()
    i = 0
    while stack:
        inst = stack.pop()
        if inst in called:
            print(inst, called)
            return acc_total
        called.add(inst)
        if inst[0] == 'nop':
            i += 1
            stack.append(I[i])
            continue
        elif inst[0] == 'acc':
            acc_total += inst[1]
            i += 1
            stack.append(I[i])
        elif inst[0] == 'jmp':
            i += inst[1]
            stack.append(I[i])
    return acc_total


def part2(I):
    stack = []
    stack.append(I[0])
    acc_total = 0
    called = set()
    i = 0
    while stack:
        try:
            inst = stack.pop()
            if inst in called:
                return 'bad'
            called.add(inst)
            if inst[0] == 'nop':
                i += 1
                stack.append(I[i])
                continue
            elif inst[0] == 'acc':
                acc_total += inst[1]
                i += 1
                stack.append(I[i])
            elif inst[0] == 'jmp':
                i += inst[1]
                stack.append(I[i])
        except IndexError as e:
            break
    return acc_total


def part2_helper(I):
    for i, inst in enumerate(I):
        cp = I[:]
        temp = list(cp[i])
        if cp[i][0] == 'nop':
            temp[0] = 'jmp'
            cp[i] = tuple(temp)
        elif cp[i][0] == 'jmp':
            temp[0] = 'nop'
            cp[i] = tuple(temp)
        else:
            continue
        result = part2(cp)
        if result == 'bad':
            continue
        else:
            return result


def solution(file):
    instructions = []
    i = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n').replace('+', '').split(' ')
            line[1] = int(line[1])
            line.append(i)
            instructions.append(tuple(line))
            i += 1
    return part2_helper(instructions)


if __name__ == '__main__':
    result = solution('input/d8.txt')
    print(result)
