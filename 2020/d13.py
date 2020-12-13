import fileinput
import sys

lines = [l.strip() for l in fileinput.input()]

# part 1
depart_time = int(lines[0])
buses = [int(l) for l in filter(lambda x: x != 'x', lines[1].split(','))]

earliest = sys.maxsize
id = 0
for bid in buses:
    t = depart_time + bid - depart_time % bid
    if t < earliest:
        earliest = t
        id = bid
print(id * (earliest - depart_time))

# part 2
time, step = 0, 1
for offset, bus in [(i, int(l)) for i, l in enumerate(lines[1].split(',')) if l != 'x']:
    while (time + offset) % bus:
        time += step
    step *= bus
print(time)
