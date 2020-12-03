# class Slope:
#
#     def __init__(self, x, y):

def count_trees(grid, x, y):
    count = 0
    x_max = len(grid[0])
    y_max = len(grid)
    x_pos, y_pos = 0, 0
    for i in range(y, len(grid), y):
        row = grid[i]
        x_pos += x
        if x_pos >= x_max:
            x_pos -= x_max
        if row[x_pos] == '#':
            count += 1
    return count

def solution(file):
    grid = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            grid.append(line)
    count = 1
    count *= count_trees(grid, 1, 1)
    count *= count_trees(grid, 3, 1)
    count *= count_trees(grid, 5, 1)
    count *= count_trees(grid, 7, 1)
    count *= count_trees(grid, 1, 2)
    return count


if __name__ == '__main__':
    result = solution('input1.txt')
    print(result)
