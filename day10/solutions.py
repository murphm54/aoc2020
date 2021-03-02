def read_file(file_name):
    # read input file
    input = open(file_name, 'r')
    lines = input.read().splitlines()
    lines = [int(i) for i in lines]
    return lines


def find_voltage_differences(voltages, jolt_range):
    # check for condtion that number is not sum of any 2 digits in previous window
    max_jolt = max(voltages) + jolt_range
    voltage_differences = [0 for x in range(jolt_range)]
    voltages.sort()
    all_valid = {}
    for j in [0] + voltages:
        possible_jolts = [1 + j + i for i in range(jolt_range)]
        search_jolts = list(set(possible_jolts) & set(voltages + [max_jolt]))
        if len(search_jolts) > 0:
            search_jolt = min(search_jolts)
            voltage_differences[search_jolt - j - 1] += 1
            all_valid.update({j: search_jolts})

    return voltage_differences, all_valid


def combination_count(valid_voltages, curr_voltage ,test):

    if len(valid_voltages.get(curr_voltage, [])) == 0:
        return 1
    # else:
    #     total_count = 1
    #     for v in valid_voltages[curr_voltage]:
    #         total_count *= combination_count(valid_voltages, v)
    #     return total_count
    # return total_count
    else:
        total_count = 0
        for i in valid_voltages[curr_voltage]:
            total_count += combination_count(valid_voltages, i, test)
        return total_count

def main():
    voltages = read_file('input.txt')
    differences, all_valid = find_voltage_differences(voltages, 3)
    print("Part 1 Answer: ", differences[0]*differences[2])
    print("Part 2 Answer: ", combination_count(all_valid, 0, []))


if __name__ == "__main__":
    main()
