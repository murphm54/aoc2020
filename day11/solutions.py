import copy


def read_file(file_name):
    input = open(file_name, 'r')
    lines = input.read().splitlines()
    return lines


def seat_iteration(seats):
    # continue changing seat layout until stabilises
    prev_seats, new_seats = None, [list(row) for row in seats]
    # offset of adjacent seats
    all_inds = [x for i in [-1, 1] for x in [[0, i], [i, 0], [i, -1*i], [i, i]]]

    while prev_seats != new_seats:
        prev_seats = new_seats
        new_seats = seat_layout(prev_seats, all_inds)

    # return count of occupied seats
    return sum([sum([c == '#' for c in r]) for r in new_seats])


def seat_layout(seats, all_inds):
    # change seat layout based on rules
    new_seats = copy.deepcopy(seats)

    for row_ind, row in enumerate(seats):
        for col_ind, curr_seat in enumerate(row):
            adj_seats = [get_seat(seats, row_ind + inds[0], col_ind + inds[1])
                         for inds in all_inds]

            if curr_seat == 'L' and all([a != '#' for a in adj_seats]):
                new_seats[row_ind][col_ind] = '#'
            elif curr_seat == '#' and sum([a == '#' for a in adj_seats]) >= 4:
                new_seats[row_ind][col_ind] = 'L'

    return new_seats


def get_seat(seats, row_ind, col_ind):
    # get seat value, return floor if out of range

    if row_ind >= len(seats) or row_ind < 0:
        return '.'
    if col_ind >= len(seats[row_ind]) or col_ind < 0:
        return '.'
    else:
        return(seats[row_ind][col_ind])


def main():
    seats = read_file('input.txt')
    print("Part 1 Answer: ", seat_iteration(seats))
    #print("Part 2 Answer: ", combination_count(all_valid))


if __name__ == "__main__":
    main()
