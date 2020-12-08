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


def find_bag(rules, curr_bag, search_bag):
    # recursively seach for a given bag
    if len(rules[curr_bag].keys()) == 0:
        return False
    else:
        bag_found = False
        bag_found = search_bag in rules[curr_bag].keys()
        if not bag_found:
            for bag in rules[curr_bag].keys():
                bag_found = bag_found or find_bag(rules, bag, search_bag)

        return bag_found


def search_all_bags(rules, search_bag):
    # search for a given bag in all paths
    all_bags = []
    for r in rules.keys():
        all_bags.append(find_bag(rules, r, search_bag))
    return sum(all_bags)


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


def main():
    rules = read_file('input.txt')
    print("Part 1 Answer: ", search_all_bags(rules, 'shiny gold'))
    print("Part 2 Answer: ", calc_bag(rules, rules['shiny gold']))


if __name__ == "__main__":
    main()
