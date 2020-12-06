from collections import defaultdict

def solution(file):
    count = 0
    data = defaultdict(set)
    init = False
    with open(file) as f:
        for row in f:
            row = row.rstrip('\n')
            if not row:
                count += 1
                init = False
            else:
                # part 1
                # for letter in row:
                #     data[count].add(letter)
                if not init:
                    for letter in row:
                        data[count].add(letter)
                    init = True
                else:
                    data[count] = data[count].intersection(set(list(row)))
    count = 0
    for i, k in enumerate(data):
        count += len(data[k])
    return count


if __name__ == '__main__':
    result = solution('input/d6.txt')
    print(result)
