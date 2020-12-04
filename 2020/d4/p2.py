import re

def checkKeys(keys, data):
    for key in keys:
        if key not in data:
            return False
    if int(data['byr']) < 1920 or int(data['byr']) > 2002:
        return False
    if int(data['iyr']) < 2010 or int(data['iyr']) > 2020:
        return False
    if int(data['eyr']) < 2020 or int(data['eyr']) > 2030:
        return False
    if not (data['hgt'].endswith('cm') or data['hgt'].endswith('in')):
        return False
    if data['hgt'][-2:] == 'cm' and (int(data['hgt'][:-2]) > 193 or int(data['hgt'][:-2]) < 150):
        return False
    if data['hgt'][-2:] == 'in' and (int(data['hgt'][:-2]) > 76 or int(data['hgt'][:-2]) < 59):
        return False
    if not re.match(r'^#[0-9a-f]{6}$', data['hcl']):
        return False
    if not data['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not re.match(r'^[0-9]{9}$', data['pid']):
        return False
    return True

def solution(file):
    count = 0
    data = {}
    valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = []
    with open(file) as f:
        for row in f:
            row = row.rstrip('\n')
            if not row:
                passports.append(data)
                data = {}
            else:
                pairs = row.split(' ')
                for pair in pairs:
                    data[pair[:3]] = pair[4:]
    passports.append(data)
    for passport in passports:
        if checkKeys(valid, passport):
            count += 1
    return count


if __name__ == '__main__':
    result = solution('input.txt')
    print(result)
