def read_file(file_name):
    input_file = open(file_name, 'r').read().splitlines()
    rule_dict = {}
    for line in input_file:
        rule, args = line.split(':')[0:2]
        match_rules = args.strip().split('|')
        formatted_match_rules = []
        for match_rule in match_rules:
            formatted_match_rules.append(match_rule.strip().replace('"','').split(' '))
        rule_dict.update({rule: formatted_match_rules})
    return rule_dict

def find_possible_matches(rule_dict):
    for rule_key in rule_dict.keys():
        res = rule_match(rule_dict, rule_dict[rule_key])
        print(res)


def rule_match(rule_dict, rules):
    all_options = []
    for option in rules:
        option_string = ''
        for step in option:
            matching_rule = rule_dict.get(step, '')
            if len(matching_rule) > 1 or any([not c.isalpha() for c in matching_rule[0][0]]):
                child_strings = rule_match(rule_dict, matching_rule)
                all_options = [option_string + x for x in child_strings]
            else:
                option_string = option_string + matching_rule[0][0]
        all_options.append(option_string)
    return all_options 
    
def rule_string(rule_dict, matching_rule):
    if len(matching_rule) > 1 or any([not c.isalpha() for c in matching_rule[0][0]]):
        matching_string = []
        matching_string = matching_string + rule_match(rule_dict, matching_rule)
        return matching_string
    else:
        return matching_rule[0][0]

def main():
    rule_dict = read_file('test.txt')
    find_possible_matches(rule_dict)
    #print("Part 1 Answer: ", calculate_strings(expression_list, calc_left_to_right))


if __name__ == "__main__":
    main()