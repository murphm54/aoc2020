def read_file(file_name):
    #r ead file, split into lines and remove empty values
    input = open(file_name, 'r')
    lines = input.read().split("\n\n")
    entries = [[r for r in line.split("\n") if r] for line in lines]
    return entries


def calc_yes_any(line):
    # calculate count of distinct elements of lists
    return len(set(''.join(line)))


def calc_yes_all(line):
    # calculate count of interesection of elements in list
    return len(set.intersection(*map(set, line)))


def calc_yes(lines, func):
    # calculate sum of results of function provided
    yes_length = [func(line) for line in lines]
    return sum(yes_length)


def main():
    entries = read_file('input.txt')
    print("Part 1 Answer: ", calc_yes(entries, calc_yes_any))
    print("Part 2 Answer: ", calc_yes(entries, calc_yes_all))


if __name__ == "__main__":
    main()
