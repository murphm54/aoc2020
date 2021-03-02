import re
import itertools
import copy


def read_file(file_name):
    input_file = open(file_name, 'r').read().splitlines()
    all_steps = []
    ind = -1
    reg = re.compile("mask*")
    for i in input_file:
        broken_string = [x.strip() for x in i.split('=')]
        if bool(re.match(reg, broken_string[0])):
            all_steps.append([broken_string[1], []])
            ind += 1
        else:
            all_steps[ind][1].append([int(broken_string[1]),
                                      int(broken_string[0][4:][:-1])])

    return all_steps


def decimal_to_bit_list(decimal, length):
    blank_mask = length * '0'
    return [x for x in (blank_mask + str(bin(decimal))[2:])[-1*length:]]


def system_one(addr, value, mask, mask_length, mem_addresses):

    bit_values = decimal_to_bit_list(value, mask_length)
    for ind, mask_value in enumerate(mask):
        if mask_value != 'X':
            bit_values[ind] = mask_value
    mem_addresses.update({addr: int(''.join(bit_values), 2)})

    return mem_addresses


def system_two(addr, value, mask, mask_length, mem_addresses):

    bit_values = decimal_to_bit_list(addr, mask_length)

    for ind, mask_value in enumerate(mask):
        if mask_value != '0':
            bit_values[ind] = mask_value

    comb_length = sum([int(b == 'X') for b in bit_values])
    all_combinations = [(list(i)) for i 
                        in list(itertools.product(('01'), repeat=comb_length))]

    for comb in all_combinations:
        comb_bit_values = copy.deepcopy(bit_values)
        X_count = 0
        for enum, item in enumerate(comb_bit_values):
            if item == 'X':
                comb_bit_values[enum] = comb[X_count]
                X_count += 1
        new_sum = int(''.join(comb_bit_values), 2)
        mem_addresses.update({new_sum: value})

    return mem_addresses


def docking_initialisation(all_steps, docking_version):
    mem_addresses = dict()
    for step in all_steps:
        mask = step[0]
        mask_length = len(mask)
        for value, addr in step[1]:
            if docking_version == 1:
                mem_addresses = system_one(addr, value, mask, mask_length, mem_addresses)
            else:
                mem_addresses = system_two(addr, value, mask, mask_length, mem_addresses)
    return sum(mem_addresses.values())


def main():
    all_steps = read_file('input.txt')
    print("Part 1 Answer: ", docking_initialisation(all_steps, 1))
    print("Part 2 Answer: ", docking_initialisation(all_steps, 2))


if __name__ == "__main__":
    main()
