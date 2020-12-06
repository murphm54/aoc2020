
def read_file(file_name):
    # read input file and cast to int
    lines = open(file_name, 'r')
    return [int(r) for r in lines.read().splitlines()]


def find_two_2020(lines):
    # find product of two entries when added together equal 2020
    res = None
    for ind, i in enumerate(lines):
        if res is not None:
            break
        lines_copy = lines[:]
        lines_copy.pop(ind)
        for j in lines_copy:
            if i + j == 2020:
                res = i * j
    return res


def find_three_2020(lines):
    # find product of three  entries when added together equal 2020
    res = None
    for ind1, i in enumerate(lines):
        if res is not None:
            break
        for ind2, j in enumerate(lines):
            lines_copy = lines[:]
            inds = [ind1, ind2]
            inds.sort(reverse=True)
            [lines_copy.pop(x) for x in inds]
            for k in lines_copy:
                if i + j + k == 2020:
                    res = i * j * k
    return res


def main():
    lines = read_file('input.txt')
    print("Part 1 answer: ", find_two_2020(lines))
    print("Part 2 answer: ", find_three_2020(lines))


if __name__ == "__main__":
    main()
