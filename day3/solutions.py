def read_file(file_name):
    # read input file and split each into lines,
    input = open(file_name, 'r')
    lines = input.read().splitlines()
    return lines


def count_trees(lines, step_right, step_down):
    # count number of trees encountered
    # when following steps until bottom of grid
    row, col, trees = 0, 0, 0

    while row < len(lines) - step_down:
        col += step_right
        row += step_down
        row_length = len(lines[row-step_down])
        if col >= row_length:
            col = col - row_length
        if lines[row][col] == '#':
            trees += 1

    return trees


def main():
    lines = read_file('input.txt')
    print("Part 1 answer: ", count_trees(lines, 3, 1))

    part_two_inputs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    res = 1
    # count number of trees for various inputs and multiply together
    for args in part_two_inputs:
        res = res * count_trees(lines, *args)
    print("Part 2 answer: ", res)


if __name__ == "__main__":
    main()
