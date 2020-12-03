input = open('input.txt', 'r')
lines = input.read().splitlines()


def count_trees(step_right, step_down):
    row = 0
    col = 0
    trees = 0

    while row < len(lines) - step_down:
        col += step_right
        row += step_down
        row_length = len(lines[row-step_down])
        if col >= row_length:
            col = col - row_length
        if lines[row][col] == '#':
            trees += 1

    return trees


print("Part 1 Answer: ", count_trees(3, 1))

part_two_inputs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
res = 1
for args in part_two_inputs:
    res = res * count_trees(*args)

print("Part 1 Answer: ", res)
