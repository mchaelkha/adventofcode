from collections import defaultdict


def process(line, bags):
    amounts = defaultdict(int)
    left, right = [i.strip() for i in line.split('contain')]
    deps = [i.strip() for i in right.split(',')]
    for i in deps:
        ct, kind = i.split(' ', 1)
        if kind.endswith('s'):
            kind = kind[:-1]
            print(kind)
        amounts[kind] = int(ct)
    bags[left] = amounts
    return left, amounts


def part1_bfs(bags):
    gold_count = 0
    targets = set()
    targets.add('shiny gold bag')
    discovered = set()
    while targets:
        temp = set()
        for targ in targets:
            for key in list(bags.keys()):
                dict_val_keys = set(bags[key].keys())
                if not key in discovered and targ in dict_val_keys:
                    gold_count += 1
                    discovered.add(key)
                    temp.add(key)
        targets = temp
    return gold_count


def dfs(bags, targ):
    total = 0
    for key in list(bags[targ].keys()):
        ct = bags[targ][key]
        total += ct
        total += ct * dfs(bags, key)
    return total


def part2_dfs(bags):
    return dfs(bags, 'shiny gold bag')


def solution(file):
    count = 0
    bags = defaultdict(defaultdict)
    with open(file) as f:
        for line in f:
            if 'no other bags' in line:
                continue
            line = line.rstrip('\n').rstrip('.').replace('bags', 'bag')
            process(line, bags)
    return part2_dfs(bags)


if __name__ == '__main__':
    result = solution('input/d7.txt')
    print(result)
