def read_file(file_name):
    #read file and split lines 
    input = open(file_name, 'r')
    return input.read().splitlines()


def calc_adj(sel_range):
    # determine number to shift search range by
    return int((1 + (sel_range[1] - sel_range[0])) // 2)


def apply_adj(sel_range, letter):
    # adjust search range depending on clue given
    adj = calc_adj(sel_range)
    if letter in ['F', 'L']:
        sel_range[1] = sel_range[1] - adj
    if letter in ['B', 'R']:
        sel_range[0] = sel_range[0] + adj

    return sel_range


def calc_seat_id(row, col):
    # algroithm to calculate seat id
    return row * 8 + col


def find_seat(boarding_key, row_count, col_count):
    # find each seat id by narrowing down range
    row_range = [0, row_count-1]
    col_range = [0, col_count-1]

    for letter in boarding_key:
        if letter in ['F', 'B']:
            row_range = apply_adj(row_range, letter)
        else:
            col_range = apply_adj(col_range, letter)

    return calc_seat_id(row_range[0], col_range[0])


def find_missing_seat(all_seat_ids):
    # find missing seat id
    for id in all_seat_ids:
        if (not (id + 1) in all_seat_ids) and (id + 2) in all_seat_ids:
            return(id + 1)
    return 0


def main():
    lines = read_file('input.txt')
    all_seat_ids = []
    for line in lines:
        all_seat_ids.append((find_seat(line, 128, 8)))
    print("Part 1 answer: ", max(all_seat_ids))
    print("Part 2 answer: ", find_missing_seat(all_seat_ids))


if __name__ == "__main__":
    main()
