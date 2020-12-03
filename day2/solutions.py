file1 = open('input.txt', 'r')
Lines = file1.readlines()

rules, chars, passwords = [[], [], []]

valid_passwords = 0
count = 0

for line in Lines:
    line_list = line.split(" ")
    rules.append([int(x) for x in line_list[0].split("-")])
    chars.append(line_list[1].replace(":", ""))
    passwords.append(line_list[2].replace("\n", ""))

for i in range(len(passwords)):
    char_count = passwords[i].count(chars[i])
    if rules[i][0] <= char_count <= rules[i][1]:
        valid_passwords += 1

print("Part 1 Answer: ", valid_passwords)

valid_passwords = 0

for i in range(len(passwords)):
    char_count = sum([chars[i] == passwords[i][j-1] for j in rules[i]])
    if char_count == 1:
        valid_passwords += 1

print("Part 2 Answer: ", valid_passwords)
