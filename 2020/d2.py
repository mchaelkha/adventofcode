class Policy:

    # part 1
    # def __init__(self, rule):
    #     temp = rule.split('-')
    #     self.min_char, self.max_char = int(temp[0]), int(temp[1][0:-2])
    #     self.char = temp[1][-1]
    #
    #
    # def check_password(self, password):
    #     char_count = password.count(self.char)
    #     return char_count >= self.min_char and char_count <= self.max_char

    def __init__(self, rule):
        temp = rule.split('-')
        self.positions = [int(temp[0]), int(temp[1][0:-2])]
        self.char = temp[1][-1]


    def check_password(self, password):
        return (password[self.positions[0]] == self.char) \
            != (password[self.positions[1]] == self.char)



def is_corrupt(parts):
    return not Policy(parts[0]).check_password(parts[1])


def solution(file):
    count = 0
    with open(file) as f:
        for line in f:
            parts = line.strip().split(':')
            if not is_corrupt(parts):
                count += 1
    return count


if __name__ == '__main__':
    result = solution('input/d2.txt')
    print(result)
