import copy

def read_file(file_name):
    input = open(file_name, 'r')
    earliest_time, buses = input.read().splitlines()
    buses = [[ind, int(b)] for ind, b in enumerate(buses.split(',')) if b != 'x']
    return int(earliest_time), buses


def find_bus(earliest_time, buses):

    bus_time = copy.deepcopy(earliest_time)
    bus_found = None
    while bus_found is None:
        for b in buses:
            if bus_time % b == 0:
                bus_found = b * (bus_time - earliest_time)
        bus_time += 1
    return bus_found

def find_time(buses):

    match_time = 939
    offsets = [b[0] for b in buses]
    time_found = None
    while time_found is None:
        all_times = [match_time + o for o in offsets]
        all_times[1:]
        print("here")


def main():
    earliest_time, buses = read_file('test.txt')
    print("Part 1 Answer: ", find_bus(earliest_time, [b[1] for b in buses]))
    print("Part 2 Answer: ", find_time(buses))


if __name__ == "__main__":
    main()
