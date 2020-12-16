import fileinput
from collections import defaultdict
import itertools

lines = [l.strip() for l in fileinput.input()]

# part 1
def apply_mask(mask, addr):
    addr |= int(mask.replace('X', '0'), 2)
    addr &= int(mask.replace('X', '1'), 2) 
    return addr

mem = defaultdict(int)
mask = ''
for l in lines:
    if l.startswith('mask'):
        mask = l.split(' = ')[1]
    else:
        a, b = l.split(' = ')
        a, b = int(a[4:-1]), int(b)
        mem[a] = apply_mask(mask, b)

print(sum(mem.values()))

# part 2
def combine(mask, value):
    ret = ''
    diff = len(mask) - len(value)
    for i, v in enumerate(mask):
        if i < diff:
            ret += v
            continue
        o = value[i - diff]
        if v == 'X':
            ret += 'X'
        elif v == o:
            ret += v
        elif o == '1' or v == '1':
            ret += '1'
    return ret

mem = defaultdict(int)
mask = ''
xs = []
for l in lines:
    if l.startswith('mask'):
        mask = l.split(' = ')[1]
        xs = []
        for i, c in enumerate(mask):
            if c == 'X':
                xs.append(i)
    else:
        a, b = l.split(' = ')
        a, b = int(a[4:-1]), int(b)
        c = combine(mask, bin(a)[2:])
        for combs in itertools.product('10', repeat=len(xs)):
            val = list(c)
            for i, comb in enumerate(combs):
                val[xs[i]] = comb[0]
            addr = int(''.join(val), 2)
            mem[addr] = b

print(sum(mem.values()))
