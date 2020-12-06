import re


def read_file(file_name):
    # read file and split into  list of dictionaries of arguments
    lines = open(file_name, 'r')
    lines = lines.read().split("\n\n")
    all_passports = []
    for line in lines:
        attributes = line.replace("\n", " ").split(" ")
        all_passports.append(
            {k: v for k, v in [a.split(":") for a in attributes if a]})
    return all_passports


def range_check(field, min_field, max_field):
    # check if field value within range
    return min_field <= int(field) <= max_field


def eye_check(field):
    # check if eye colour in list of valid values
    return field in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def pattern_check(field, regex):
    # check if field matches regex required
    return bool(regex.match(field))


def height_check(field):
    # check if correct regex and numeric value within range
    format_pass = pattern_check(field, re.compile('[0-9]+(cm|in)'))
    range_pass = False

    if format_pass:
        if field[-2:] == 'cm':
            range_pass = range_check(field[:-2], 150, 193)
        else:
            range_pass = range_check(field[:-2], 59, 76)
    return range_pass and format_pass


def check_present(passports, key_list):
    # check if all required keys exist in passport attributes
    present_passports = []
    for d in passports:
        if all([k in d.keys() for k in key_list]):
            present_passports.append(d)
    return present_passports


def check_valid(passports, func_dict):
    # check if all entries pass format requirements
    valid_passports = []
    for d in passports:
        key_check = []
        key_test = []
        for k in d.keys():
            check = func_dict.get(k, None)
            if check is not None:
                key_test.append(k)
                key_check.append(check[0](*[d[k]]+check[1]))
        if all(key_check):
            valid_passports.append(d)
    return valid_passports


def main():
    # define key checks and functions
    func_dict = {'byr': [range_check, [1920, 2002]],
                 'iyr': [range_check, [2010, 2020]],
                 'eyr': [range_check, [2020, 2030]],
                 'hgt': [height_check, []],
                 'hcl': [pattern_check, [re.compile(r'#\b([a-z0-9]{6})\b')]],
                 'ecl': [eye_check, []],
                 'pid': [pattern_check, [re.compile(r'\b([0-9]{9})\b')]]
                 }

    # read input file
    all_passports = read_file('input.txt')
    # check if all required keys exist
    present_passports = check_present(all_passports, func_dict.keys())
    print("Part 1 Answer: ",  len(present_passports))

    valid_passports = check_valid(present_passports, func_dict)
    print("Part 2 Answer: ",  len(valid_passports))


if __name__ == "__main__":
    main()
