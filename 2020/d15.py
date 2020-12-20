from collections import defaultdict

# nums = [0,3,6]
nums = [20,0,1,11,6,3]
cache = defaultdict(lambda: -1)
for i, v in enumerate(nums[:-1]):
    cache[v] = i

while len(nums) < 30000000:
    prev = nums[-1]
    prev_turn = cache[prev]
    cache[prev] = len(nums) - 1
    if prev_turn == -1:
        nums.append(0)
    else:
        nums.append(len(nums) - 1 - prev_turn)
    # part 1
    if len(nums) == 2020:
        print(len(nums) - 2 - prev_turn)
# part 2
print(nums[-1])
print('actual:', 421, 436)
