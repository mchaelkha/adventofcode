def part1(A):
    jolt_1 = 0
    jolt_3 = 0
    A.sort()
    for i in range(1, len(A)):
        if A[i] - A[i - 1] == 1:
            jolt_1 += 1
        elif A[i] - A[i - 1] == 3:
            jolt_3 += 1
    return (jolt_1 + 1) * (jolt_3 + 1)


def is_valid(A):
    for i in range(1, len(A)):
        if A[i] - A[i - 1] > 3:
            return False
    return True


def find_next(A, i, start=False):
    curr = A[i] if not start else 0
    poss = []
    for j in range(i + 1, len(A)):
        if A[j] - curr <= 3:
            poss.append(j)
        else:
            break
    return poss


def dfs(A, curr, disc, i):
    if curr and curr[-1] == A[-1]:
        disc.add(tuple(curr))
        return
    vals = find_next(A, i)
    for v in vals:
        temp = curr[:]
        temp.append(A[v])
        dfs(A, temp, disc, v)
    return disc


def part2_dfs(A):
    A.sort()
    target = A[-1]
    A = tuple(A)
    disc = set()
    vals = find_next(A, -1, start=True)
    total = 0
    for v in vals:
        res = dfs(A, [A[v]], disc, v)
        disc.union(res)
    return len(disc)


def part2_dp(A):
    A.sort()
    dp = [0] * (1 + A[-1])
    dp[0] = 1
    # how many ways to climb n stairs with 1-3 steps 
    for n in A:
        dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]
    return dp[-1]


def solution(file):
    count = 0
    adapters = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            adapters.append(int(line))
    return part2_dp(adapters)


if __name__ == '__main__':
    result = solution('input/d10.txt')
    print(result)
