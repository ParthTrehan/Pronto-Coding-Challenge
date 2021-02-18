import argparse
import re


def get_parser():
    prog = """robot.py"""

    description = """
    description:
    This is a simple program that takes a string
    of commands as inputs and produces the robot's
    distance from it's starting point.
    """
    commands_help = """
    a string of comma-separated commands eg: "F1,R1,B2,L1,B3"
    """
    parser = argparse.ArgumentParser(
        prog=prog,
        description=description)
    parser.add_argument('--commands', '-c', type=str,
                        required=True, help=commands_help)
    parser.add_argument('--verbose', '-v', action='store_true', default=False)
    return parser


def error(err):
    print('error: ' + err)
    exit(0)


def logger(verbose=False, *argv):
    if verbose:
        print(*argv)


def commands_validator(commands):
    if not(re.match(pattern="^([F|B|R|L][1-9])(,[F|B|R|L][1-9])*$", string=commands)):
        error('Invalid input commands')


def traverse_path(commands):
    current_pos_x = 0
    current_pos_y = 0
    current_dir = 'N'
    commands_arr = commands.split(',')
    for command in commands_arr:
        if command[0] in ['F', 'B']:
            (current_pos_x, current_pos_y) = move_robot(
                command, current_pos_x, current_pos_y, current_dir)
        else:
            current_dir = rotate_robot(command, current_dir)
    return(current_dir, (current_pos_x, current_pos_y))


def move_robot(command, current_pos_x, current_pos_y, current_dir):
    if command[0] == 'F':
        if current_dir == 'N':
            current_pos_y += int(command[1])
        elif current_dir == 'E':
            current_pos_x += int(command[1])
        elif current_dir == 'S':
            current_pos_y -= int(command[1])
        else:
            current_pos_x -= int(command[1])
    else:
        if current_dir == 'N':
            current_pos_y -= int(command[1])
        elif current_dir == 'E':
            current_pos_x -= int(command[1])
        elif current_dir == 'S':
            current_pos_y += int(command[1])
        else:
            current_pos_x += int(command[1])
    return (current_pos_x, current_pos_y)


def rotate_robot(command, current_dir):
    direction_arr = ['N', 'E', 'S', 'W']
    direction_units = int(command[1]) % 4
    if command[0] == 'L':
        current_dir = direction_arr[direction_arr.index(
            current_dir)-direction_units]
    else:
        current_dir = direction_arr[direction_arr.index(
            current_dir)+direction_units]
    return current_dir


def calculate_distance(current_position):
    current_pos_x, current_pos_y = current_position
    return (abs(current_pos_x) + abs(current_pos_y))


if __name__ == '__main__':
    args = get_parser().parse_args()
    verboseprint = print if args.verbose else lambda *a, **k: None

    commands_validator(args.commands)
    current_dir, current_position = traverse_path(args.commands)
    distance = calculate_distance(current_position)

    verboseprint('current direction - ', current_dir)
    verboseprint('current position  - ', current_position)
    verboseprint('distance to start - ', distance)

    print(distance)
