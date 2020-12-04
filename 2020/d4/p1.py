import re

def checkKeys(keys, data):
    for key in keys:
        if key not in data:
            return False
    return True

def solution(file):
    count = 0
    data = {}
    valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    with open(file) as f:
        for row in f:
            row = row.rstrip('\n')
            if not row:
                if checkKeys(valid, data):
                    count += 1
                data = {}
            else:
                # process
                pairs = row.split(' ')
                for pair in pairs:
                    data[pair[:3]] = pair[4:]
    if checkKeys(valid, data):
        count += 1
    return count


if __name__ == '__main__':
    result = solution('input.txt')
    print(result)
