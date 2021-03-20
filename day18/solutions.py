OPERATORS = "+-%*"
OPERATOR_DICT = op = {'+': lambda x, y: x + y,
                      '-': lambda x, y: x - y,
                      '*': lambda x, y: x * y,
                      '%': lambda x, y: x % y}


def read_file(file_name):
    input_file = open(file_name, 'r').read().splitlines()
    return input_file


def calculate_strings(expression_list, precedence_function):
    # calculate each line in input file
    total_sum = 0
    for expression in expression_list:
        total_sum += calc_by_brackets(expression, precedence_function)
    return total_sum


def calc_addition_first(calc_string):
    # exeute addition operators before others

    while any([x in OPERATORS for x in calc_string]):
        addition_indices = get_true_indices([x == '+' for x in calc_string])
        other_operator_indices = OPERATORS.replace('+','')
        other_operator_indices = get_true_indices([x in other_operator_indices for x in calc_string])
        all_operator_indices = addition_indices + other_operator_indices
        operator_ind = all_operator_indices[0]
        function = OPERATOR_DICT[calc_string[operator_ind]]

        prev_operators = [x for x in all_operator_indices if x < operator_ind]
        if len(prev_operators):
            prev_operators.sort(reverse=True)
            prev_operator = prev_operators[0]
        else:
            prev_operator = 0

        next_operators = [x for x in all_operator_indices if x > operator_ind]
        if len(next_operators):
            next_operators.sort()
            next_operator = next_operators[0]
        else:
            next_operator = len(calc_string)

        first_argument = get_arguments(calc_string,
                                       prev_operator,
                                       operator_ind)

        second_argument = get_arguments(calc_string,
                                        operator_ind,
                                        next_operator)

        new_calc_string = str(function(first_argument, second_argument)) + \
            calc_string[next_operator:]

        if prev_operator == 0:
            calc_string = new_calc_string
        else:
            calc_string = calc_string[:prev_operator+1] + new_calc_string

    return int(calc_string.strip())


def calc_left_to_right(calc_string):
    operator_indices = get_true_indices([x in OPERATORS for x in calc_string])
    current_sum = get_arguments(calc_string, 0, operator_indices[0])
    for list_ind, operator_ind in enumerate(operator_indices):
        function = OPERATOR_DICT[calc_string[operator_ind]]
        second_argument = get_arguments(calc_string,
                                        operator_ind,
                                        (operator_indices+[len(calc_string)])
                                        [list_ind+1])
        current_sum = function(current_sum, second_argument)

    return current_sum

def calc_by_brackets(calc_string, precedence_function):

    # check for unmatched brackets    
    opening_brackets = find_char_in_string(calc_string, '(')
    closing_brackets = find_char_in_string(calc_string, ')')

    if len(opening_brackets) != len(closing_brackets):
        print('brackets are unmatched')

    while len(find_char_in_string(calc_string, '(')):
        opening_brackets = find_char_in_string(calc_string, '(')

        for bracket in opening_brackets:
            next_closing_bracket = [ind for ind in find_char_in_string(calc_string, ')') if ind > bracket][0]
            next_opening_brackets = [ind for ind in find_char_in_string(calc_string, '(') if ind > bracket]

            # set to end of string if no next opening bracket
            if len(next_opening_brackets):
                next_opening_bracket = next_opening_brackets[0]
            else:
                next_opening_bracket = len(calc_string) + 1

            # matching bracket has been found, calculate string in brackets
            # and update larger string
            if next_closing_bracket < next_opening_bracket:
                sub_calc = calc_string[bracket + 1:next_closing_bracket]
                calc_string = calc_string[:bracket] + \
                    str(precedence_function(sub_calc)) + \
                    calc_string[next_closing_bracket+1:]
                break

    return precedence_function(calc_string)


def find_char_in_string(string, char):
    # find indices where characters exist in string
    return get_true_indices([c == char for c in string])


def get_true_indices(boolean_list):
    # get indices of true elements in list
    return [i for i, x in enumerate(boolean_list) if x]


def get_arguments(calc_string, first_ind, second_ind):
    # slice string and remove operators/empty spaces if exist
    argument = calc_string[first_ind:second_ind]
    return int(''.join([c for c in argument if c not in OPERATORS]).strip())


def main():
    expression_list = read_file('input.txt')
    print("Part 1 Answer: ", calculate_strings(expression_list, calc_left_to_right))
    print("Part 2 Answer: ", calculate_strings(expression_list, calc_addition_first))


if __name__ == "__main__":
    main()