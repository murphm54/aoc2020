def convert_to_int_list(input_list):
    return [int(x) for x in input_list]


def read_file(file_name):
    input_file = open(file_name, 'r').read().split('\n\n')
    input_categories = [x.splitlines() for x in input_file]
    all_rules = dict()

    for rule in input_categories[0]:
        rule_split = rule.split(':')
        num_ranges = rule_split[1].split('or')
        formatted_ranges = []
        for num_range in num_ranges:
            formatted_ranges.append(
                convert_to_int_list(num_range.strip().split('-')))
        all_rules[rule_split[0]] = formatted_ranges

    my_ticket = convert_to_int_list(input_categories[1][1].split(','))
    nearby_tickets = []
    for ticket in input_categories[2][1:]:
        nearby_tickets.append(convert_to_int_list(ticket.split(',')))

    return all_rules, my_ticket, nearby_tickets


def check_valid_tickets(all_rules, my_ticket, nearby_tickets):
    invalid_nums = 0
    for ticket in nearby_tickets:
        for num in ticket:
            valid_checks = dict(zip(list(all_rules.keys()), [False, False, False]))
            for rule in all_rules.keys():
                for num_range in all_rules[rule]:
                    #if valid_checks[rule]:
                    #    break
                    if num_range[0] <= num <= num_range[1]:
                        valid_checks[rule] = True
                        break
            print(valid_checks)
            if not any(valid_checks.values()):
                invalid_nums += num

    return invalid_nums


def main():
    all_rules, my_ticket, nearby_tickets = read_file('input.txt')
    print("Part 1 Answer: ", check_valid_tickets(all_rules, my_ticket, nearby_tickets))


if __name__ == "__main__":
    main()