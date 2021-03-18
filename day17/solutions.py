import copy

def read_file(file_name):
    input_file = open(file_name, 'r').read().splitlines()
    initial_state = []
    for line in input_file:
        initial_state.append([x for x in line])
    return [initial_state]

def get_cube_dimensions(state, dimension):
    dim_1_count = len(state)
    dim_2_count = len(state[0])
    dim_3_count = len(state[0][0])
    if dimension == 3:
        return dim_1_count, dim_2_count, dim_3_count
    else:
        dim_4_count = len(state[0][0][0])
        return dim_1_count, dim_2_count,  dim_3_count, dim_4_count



def pad_cube(state):
    pane_count, row_count, column_count = get_cube_dimensions(state, 3)
    blank_pane = []
    for column in range(column_count):
        blank_pane.append(['.' for row in range(row_count)])
    state = [blank_pane] + state + [blank_pane]
    pane_count, row_count, column_count = get_cube_dimensions(state, 3)
    for pane_ind, pane in enumerate(state):
        blank_row = ['.' for r in range(column_count)]
        state[pane_ind] = [blank_row] + state[pane_ind] + [blank_row] 
        for row_ind, row in enumerate(state[pane_ind]):
            state[pane_ind][row_ind] = ['.'] + row + ['.']   
         
    return state

def pad_cube_2(state):
    w_count, z_count, x_count, y_count = get_cube_dimensions(state, 4)
    blank_window = copy.deepcopy(state)
    for w in range(w_count):
        for z in range(z_count):
            for x in range(x_count):
                for y in range(y_count):
                    blank_window[w][z][x][y] = '.'
 
    state = blank_window + state + blank_window
    w_count, z_count, x_count, y_count = get_cube_dimensions(state, 4)
    
    blank_pane = []
    for y in range(y_count):
        blank_pane.append(['.' for row in range(x_count)])
    for window_ind, window in enumerate(state):
        state[window_ind] = [blank_pane] + window + [blank_pane]
   
    w_count, z_count, x_count, y_count = get_cube_dimensions(state, 4)
    
    for window_ind, window in enumerate(state):
        for pane_ind, pane in enumerate(window):
            blank_row = ['.' for r in range(y_count)]
            state[window_ind][pane_ind] = [blank_row] + state[window_ind][pane_ind] + [blank_row] 
            for row_ind, row in enumerate(state[window_ind][pane_ind]):
                state[window_ind][pane_ind][row_ind] = ['.'] + row + ['.']   
            
    return state


def cycle(state):

    state = pad_cube(state)
    new_state = copy.deepcopy(state)
    for z, pane in enumerate(state):
        for x, line in enumerate(pane):
            for y, cell in enumerate(line):
                all_coords = []
                for a in create_coords(z):
                    for b in create_coords(x):
                        for c in create_coords(y):
                            all_coords.append([a, b, c])
                if [z, x, y] in all_coords:
                    all_coords.remove([z, x, y])
                neighbour_active = sum([get_coord(state, *cell) for cell in all_coords])
                current_state = get_coord(state, z, x, y)
                if current_state and neighbour_active not in [2, 3]:
                    new_state[z][x][y] = '.'
                elif not current_state and neighbour_active == 3:
                    new_state[z][x][y] = '#'

    return new_state

def get_neighbouring_coords(w, z, x, y):

    neighbouring_coords = []
    for a in create_coords(w):
        for b in create_coords(z):
            for c in create_coords(x):
                for d in create_coords(y):
                    neighbouring_coords.append([a, b, c, d])

    if [w, z, x, y] in neighbouring_coords:
        neighbouring_coords.remove([w, z, x, y])
    
    return neighbouring_coords


def cycle_2(state):

    state = pad_cube_2(state)
    new_state = copy.deepcopy(state)
    for w, window in enumerate(state):
        for z, pane in enumerate(window):
            for x, line in enumerate(pane):
                for y, cell in enumerate(line):
                    if w ==1 and z ==1 and x ==1:
                        None
                        #print("test")
                    neighbouring_coords = get_neighbouring_coords(w, z, x, y)
                    neighbour_active = sum([get_coord_2(state, *cell) for cell in neighbouring_coords])
                    current_state = get_coord_2(state, w, z, x, y)
                    if current_state:
                        None
                        #print("here")
                    if current_state and neighbour_active not in [2, 3]:
                        new_state[w][z][x][y] = '.'
                    elif not current_state and neighbour_active == 3:
                        new_state[w][z][x][y] = '#'

    return new_state


def create_coords(i):
    return [i + n for n in [-1, 0, 1]]


def get_coord(state, z, x, y):
    z_count, x_count, y_count = get_cube_dimensions(state, 3)

    if x < 0 or x >= x_count or y < 0 or y >= y_count or z < 0 or z >= z_count:
        return False
    else:
        cell_state = state[z][x][y]
        if cell_state == '#':
            return True
        else:
            return False

    return False


def get_coord_2(state, w, z, x, y):
    w_count, z_count, x_count, y_count = get_cube_dimensions(state, 4)

    if x < 0 or x >= x_count or y < 0 or y >= y_count or z < 0 or z >= z_count or w < 0 or w >= w_count:
        return False
    else:
        cell_state = state[w][z][x][y]
        if cell_state == '#':
            return True
        else:
            return False

    return False


def part_one(initial_state):
    state = initial_state
    for i in range(6):
        state = cycle(state)
    return get_active_count(state)

def part_two(initial_state):
    state = initial_state
    for i in range(6):
        state = cycle_2(state)
        print([i, get_active_count(state)])

    return get_active_count(state)



def get_active_count(state):
    total_active = 0

    if type(state) == str:
        if state == '#':
            return 1
    else:
        for i in state:
            total_active += get_active_count(i)
    return total_active

def main():
    initial_state = read_file('test.txt')
    print("Part 1 Answer: ", part_one(initial_state))
    
    print("Part 2 Answer: ", part_two([initial_state]))



if __name__ == "__main__":
    main()