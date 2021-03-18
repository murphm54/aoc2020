import copy


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
                    if num_range[0] <= num <= num_range[1]:
                        valid_checks[rule] = True
                        break
            if not any(valid_checks.values()):
                invalid_nums += num

    return invalid_nums

def solve_code(all_rules, my_ticket, nearby_tickets):
    valid_tickets = copy.deepcopy(nearby_tickets)
    valid_tickets.append(my_ticket)
    for ind, ticket in enumerate(nearby_tickets):
        for num in ticket:
            valid_checks = False
            for rule in all_rules.keys():
                for num_range in all_rules[rule]:
                    if valid_checks:
                        break
                    if num_range[0] <= num <= num_range[1]:
                        valid_checks = True
                        break
            if not valid_checks:
                valid_tickets.remove(ticket)
                break

    ticket_length = range(len(valid_tickets[0]))
    matching_rules = [dict() for x in ticket_length]

    for ind in range(len(valid_tickets[0])):
        for ticket_ind, ticket in enumerate(valid_tickets):
            for rule in all_rules.keys():
                for num_range in all_rules[rule]:
                    if num_range[0] <= ticket[ind] <= num_range[1]:
                        ticket_rules = matching_rules[ind].get(ticket_ind, [])
                        ticket_rules.append(rule)
                        matching_rules[ind].update({ticket_ind: ticket_rules})
    
    result_set = {}
    for match_ind, match_set in enumerate(matching_rules):
        match_list = list(match_set.values())
        result = list(set(match_list[0]).intersection(*match_list[1:]))
        for item in result:
            item_lookup = result_set.get(item, [])
            item_lookup.append(my_ticket[match_ind])
            result_set[item] = item_lookup

    end_result = recursive_check(result_set)
    total_sum = 1

    for x in my_ticket:
        y = end_result[x]
        if y.startswith('departure'):
            total_sum *= x

    return total_sum

def recursive_check(recursive_set):
    end_result = {}

    while len(end_result.values()) < len(recursive_set.keys()):
        remaining_keys = [x for x in recursive_set.keys() if x not in end_result.values()]
        for k in remaining_keys:
            if len(recursive_set[k]) == 1:
                index = recursive_set[k][0]
                end_result[index] = k
                other_keys = [n for n in list(recursive_set.keys()) if n != k]
                for v in other_keys:
                    if index in recursive_set[v]:
                        recursive_set[v].remove(index)

    return end_result


def main():
    all_rules, my_ticket, nearby_tickets = read_file('input.txt')
    print("Part 1 Answer: ", check_valid_tickets(all_rules, my_ticket, nearby_tickets))
    print("Part 2 Answer: ", solve_code(all_rules, my_ticket, nearby_tickets))


if __name__ == "__main__":
    main()