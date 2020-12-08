def read_file(file_name):
    # read file, create nested dictionary strucure for each bad description
    input = open(file_name, 'r')
    lines = input.read().splitlines()
    lines = [[r.replace('.', '') for r in line.split(" bags contain ")] for line in lines]
    rules = {line[0]: parse_description(line[1]) for line in lines}
    return rules


def parse_description(description):
    # parse description of input file
    if description == "no other bags":
        return {}
    else:
        return {r[2:]: int(r[0]) for r in
                [de.replace('bags', '').replace('bag', '').strip()
                for de in description.split(',')]}


def find_bag(rules, bag):
    # find valid paths to bag provided 
    valid_bags = []
    for r in rules.keys():
        rule_keys = [[r]]
        last_keys = [rules[r]]
        bag_found = False
        while not bag_found and max([len(k) for k in last_keys]) > 0:
            rule_keys, last_keys = get_keys(rules, rule_keys)
            for path in rule_keys:
                if path[0] != bag and bag in path and not bag_found:
                    bag_found = True
                    valid_bags.append(path)
    return valid_bags


def calc_bag(rules, curr_bag):
    # recursively call calc_bag to find number of bags
    if len(curr_bag.keys()) == 0:
        return 0
    else:
        counter = 0
        for bag in curr_bag.keys():
            add_val = curr_bag[bag]
            counter += add_val + add_val * calc_bag(rules, rules[bag])
        return counter


def get_keys(rules, rule_keys):
    # get sub keys for given dictionary
    new_rule_keys = []
    last_keys = []
    for k in rule_keys:
        sub_keys = rules[k[-1]].keys()
        if len(sub_keys) == 0:
            last_keys.append('')
        for j in sub_keys:
            new_rule_keys.append(k + [j])
            last_keys.append(j)
    return new_rule_keys, last_keys


def main():
    rules = read_file('input.txt')
    valid_paths = find_bag(rules, 'shiny gold')
    print("Part 1 Answer: ", len(valid_paths))
    print("Part 2 Answer: ", calc_bag(rules, rules['shiny gold']))


if __name__ == "__main__":
    main()
