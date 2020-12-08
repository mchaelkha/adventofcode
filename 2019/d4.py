from collections import defaultdict

def check(part, pword):
    digits = list(str(pword))
    is_adj = False
    indices = defaultdict(list)
    for i, d in enumerate(digits):
        if i == 0:
            continue
        # rule 1: always increasing
        if d < digits[i - 1]:
            return False
        # rule 2: adj digits the same
        if part == 1:
            if not is_adj and d == digits[i - 1]:
                is_adj = True
        # part 2 - updated rule 2:
        elif part == 2:
            if d == digits[i - 1]:
                indices[d].append(i)
    if part == 1:
        return is_adj
    # check indices
    if part == 2:
        for k in indices.keys():
            if len(indices[k]) == 1:
                return True
        return False


def solve(part, lower, upper):
    lower = int(lower)
    upper = int(upper)
    count = 0
    for i in range(upper - lower):
        curr = lower + i
        if check(part, curr):
            count += 1
    return count


def solution(lower, upper):
    # return solve(1, lower, upper)
    return solve(2, lower, upper)


if __name__ == '__main__':
    result = solution('235741', '706948')
    print(result)
