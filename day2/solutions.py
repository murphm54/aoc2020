def read_file(file_name):
    # read input file and split each into list of rules,
    # characters and passwords
    input = open('input.txt', 'r')
    lines = input.read().splitlines()
    rules, chars, passwords = [[], [], []]

    for line in lines:
        line_list = line.split(" ")
        rules.append([int(x) for x in line_list[0].split("-")])
        chars.append(line_list[1].replace(":", ""))
        passwords.append(line_list[2])

    return(rules, chars, passwords)


def rule_range(rules, chars, passwords):
    # calculate valid passwords where character count within range
    valid_passwords = 0
    for i in range(len(passwords)):
        char_count = passwords[i].count(chars[i])
        if rules[i][0] <= char_count <= rules[i][1]:
            valid_passwords += 1
    return valid_passwords


def rule_exact(rules, chars, passwords):
    # calculate valid passwords where character count at indiced equal one
    valid_passwords = 0
    for i in range(len(passwords)):
        char_count = sum([chars[i] == passwords[i][j-1] for j in rules[i]])
        if char_count == 1:
            valid_passwords += 1
    return valid_passwords


def main():
    rules, chars, passwords = read_file('input.txt')
    print("Part 1 answer: ", rule_range(rules, chars, passwords))
    print("Part 2 answer: ", rule_exact(rules, chars, passwords))


if __name__ == "__main__":
    main()
