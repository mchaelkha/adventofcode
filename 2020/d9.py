from collections import deque


def part1(file, length):
    pre_length = length
    nums = deque()
    seq = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            seq.append(int(line))
    # init nums
    i = 0
    while len(nums) < pre_length:
        nums.append(seq[i])
        i += 1
    for j in range(i, len(seq)):
        change = False
        for m in range(len(nums)):
            for n in range(m + 1, len(nums)):
                if nums[m] + nums[n] == seq[j]:
                    nums.popleft()
                    nums.append(seq[j])
                    change = True
                    break
            if change:
                break
        if not change:
            return seq[j], seq


def part2(target, seq):
    # sliding window
    for i in range(len(seq)):
        sum = 0
        cont = []
        for j in range(i, len(seq)):
            if sum < target:
                sum += seq[j]
                cont.append(seq[j])
            elif sum == target:
                return cont
            else:
                break
    return []

def solution(file):
    num, seq = part1(file, 25)
    print(num)
    result = part2(num, seq)
    return min(result) + max(result)


if __name__ == '__main__':
    result = solution('input/d9.txt')
    print(result)
