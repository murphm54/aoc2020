def memory_game(starting_list, max_number):

    all_steps = starting_list

    # create starting dictionary with indices of starting_list
    all_steps_dict = dict(zip(starting_list,
                              [[x + 1] for x in list(range(len(starting_list)))]))
    step_num = len(all_steps)

    while step_num < max_number:
        step = all_steps[step_num-1]
        prev_step_values = all_steps_dict.get(step, [])
        ans = None

        # apply game rules
        if step not in all_steps_dict.keys() or len(prev_step_values) <= 1:
            ans = 0
        else:
            ans = prev_step_values[-1] - prev_step_values[-2]

        all_steps.append(ans)
        ans_step_values = all_steps_dict.get(ans, [])
        step_num += 1
        ans_step_values.append(step_num)
        all_steps_dict.update({ans: ans_step_values})
    
    return all_steps[-1]


def main():
    print("Part 1 Answer: ", memory_game([1, 2, 16, 19, 18, 0], 2020))
    #print("Part 2 Answer: ", docking_initialisation(all_steps, 2))


if __name__ == "__main__":
    main()
