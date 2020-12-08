import copy


def read_file(file_name):
    # read input file and format into lists of lists for each step
    input = open(file_name, 'r')
    lines = input.read().splitlines()
    lines = [[e[0], int(e[1].replace('+', ''))] for e in
             [[r for r in line.split(" ") if r] for line in lines]]
    return lines


def calc_step(line, ind, accumulator):
    # apply rules based on action

    if line[0] == 'acc':
        accumulator += line[1]
    if line[0] == 'jmp':
        ind += line[1]
    else:
        ind += 1

    return ind, accumulator


def calc_accumulator(lines):
    # apply rules until indices are repeated or index out of range

    accumulator = 0
    ind = 0
    all_inds = []
    finite = False

    while ind not in all_inds:
        if ind >= len(lines):
            finite = True
            break
        all_inds.append(ind)
        ind, accumulator = calc_step(lines[ind], ind, accumulator)

    return accumulator, finite


def find_accumulator(lines):

    # change inputs until finite combination is achieved
    change_inds = [ind for ind, i in enumerate(lines)
                   if i[0] in ['nop', 'jmp']]
    finite = False
    accumulator = 0

    for i in change_inds:
        if finite:
            break
        test_lines = copy.deepcopy(lines)
        if test_lines[i][0] == 'nop':
            test_lines[i][0] = 'jmp'
        else:
            test_lines[i][0] = 'nop'

        accumulator, finite = calc_accumulator(test_lines)
    return accumulator


def main():
    lines = read_file('input.txt')
    print("Part 1 Answer: ", calc_accumulator(lines)[0])
    print("Part 2 Answer: ", find_accumulator(lines))


if __name__ == "__main__":
    main()
