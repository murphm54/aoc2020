import copy


def read_file(file_name):
    input = open(file_name, 'r')
    lines = input.read().splitlines()
    directions = [[line[0], int(line[1:])] for line in lines]
    return directions


def move_ship(direction, facing, pos):

    if facing >= 360:
        facing -= 360
    elif facing < 0:
        facing += 360

    cmd, step = direction

    if (cmd == 'F' and facing == 0) or cmd == 'N':
        pos[1] += step
    elif (cmd == 'F' and facing == 90) or cmd == 'E':
        pos[0] += step
    elif (cmd == 'F' and facing == 180) or cmd == 'S':
        pos[1] -= step
    elif (cmd == 'F' and facing == 270) or cmd == 'W':
        pos[0] -= step
    elif cmd == 'R':
        facing += step
    elif cmd == 'L':
        facing -= step

    return pos, facing

def facing_limit(facing):
    if facing >= 360:
        facing -= 360
    elif facing < 0:
        facing += 360
    return facing


def move_waypoint(direction, facing, pos, waypoint, waypoint_facing):

    facing = facing_limit(facing)
    waypoint_facing = [facing_limit(f) for f in waypoint_facing]


    cmd, step = direction
    if cmd == 'R':
        waypoint_facing = [f + step for f in waypoint_facing]
        waypoint = [waypoint[i] * -1 if waypoint_facing[i] in [180, 270] else waypoint[i] for i in [0, 1]]
    if cmd == 'F':
        pos = [pos[i] + waypoint[i] * step for i in [0, 1]]
    else:
        waypoint, facing = move_ship(direction, facing, waypoint)

    return waypoint, waypoint_facing, pos, facing


def ship_manhattan(directions, part, pos):

    facing = 90
    waypoint = [10, 1]
    waypoint_facing = [90, 0]
    for direction in directions:
        if part == 1:
            pos, facing = move_ship(direction, facing, pos)
        else:
            waypoint, waypoint_facing, pos, facing = move_waypoint(direction, facing, pos, waypoint, waypoint_facing)
    return sum([abs(i) for i in pos])


def main():
    directions = read_file('test.txt')
    #print("Part 1 Answer: ", ship_manhattan(directions, 1, [0, 0]))
    print("Part 2 Answer: ", ship_manhattan(directions, 2, [0, 0]))


if __name__ == "__main__":
    main()
