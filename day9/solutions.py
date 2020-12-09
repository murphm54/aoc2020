def read_file(file_name):
    # read input file
    input = open(file_name, 'r')
    lines = input.read().splitlines()
    lines = [int(i) for i in lines]
    return lines


def calc_valid(numbers, window_size):
    # check for condtion that number is not sum of any 2 digits in previous window
    for ind, n in enumerate(numbers[window_size:]):
        window_numbers = numbers[ind:ind + window_size]
        valid = False
        for i in window_numbers:
            if (n - i) in window_numbers and not valid:
                valid = True
        if not valid:
            return n
    return None


def find_window(numbers, invalid_number):
    # for a given number, find valid sliding window and return range
    for ind, n in enumerate(numbers):
        total_sum = numbers[ind]
        slider = ind + 1
        while total_sum < invalid_number and slider < len(numbers)-1:
            total_sum += numbers[slider]
            if total_sum == invalid_number:
                window = numbers[ind:slider+1]
                return min(window) + max(window)
            slider += 1
    return None


def main():
    numbers = read_file('input.txt')
    invalid_number = calc_valid(numbers, 25)
    print("Part 1 Answer: ", invalid_number)
    print("Part 2 Answer: ", find_window(numbers, invalid_number))


if __name__ == "__main__":
    main()
