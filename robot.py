import argparse
import re
import time


class Robot:
    def __init__(self, current_position, direction, start_position=None):
        (current_x, current_y) = current_position
        self.current_x = current_x
        self.current_y = current_y
        self.direction = direction
        if start_position == None:
            self.start_x = self.current_x
            self.start_y = self.current_y
        else:
            (start_x, start_y) = start_position
            self.start_x = start_x
            self.start_y = start_y


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
    parser.add_argument('--verbose', '-v',
                        action='store_true', default=False,
                        help='display more information about the robot traversal')
    parser.add_argument('--commands', '-c', type=str,
                        required=True, help=commands_help)
    return parser


def error(err):
    print('error: ' + err)
    exit(0)


def commands_validator(commands):
    if not(re.match(pattern="^([F|B|R|L][1-9])(,[F|B|R|L][1-9])*$", string=commands)):
        error('Invalid input commands')


def traverse_path(robot, commands):
    commands_arr = commands.split(',')
    for command in commands_arr:
        if command[0] in ['F', 'B']:
            robot = move_robot(command, robot)
        else:
            robot = rotate_robot(command, robot)
    return(robot)


def move_robot(command, robot):
    if command[0] == 'F':
        if robot.direction == 'N':
            robot.current_y += int(command[1])
        elif robot.direction == 'E':
            robot.current_x += int(command[1])
        elif robot.direction == 'S':
            robot.current_y -= int(command[1])
        else:
            robot.current_x -= int(command[1])
    else:
        if robot.direction == 'N':
            robot.current_y -= int(command[1])
        elif robot.direction == 'E':
            robot.current_x -= int(command[1])
        elif robot.direction == 'S':
            robot.current_y += int(command[1])
        else:
            robot.current_x += int(command[1])
    return (robot)


def rotate_robot(command, robot):
    direction_arr = ['N', 'E', 'S', 'W']
    direction_units = int(command[1])
    if command[0] == 'L':
        direction_index = (direction_arr.index(
            robot.direction) - direction_units) % 4
        robot.direction = direction_arr[direction_index]
    else:
        direction_index = (direction_arr.index(
            robot.direction) + direction_units) % 4
        robot.direction = direction_arr[direction_index]
    return robot


def calculate_distance(current_position, start_position):
    current_x, current_y = current_position
    start_x, start_y = start_position
    return (abs(current_x-start_x) + abs(current_y-start_y))


if __name__ == '__main__':
    args = get_parser().parse_args()
    verbose_print = print if args.verbose else lambda *a, **k: None

    start = time.time()
    robot = Robot(current_position=(0, 0), direction='N')
    commands_validator(args.commands)
    robot = traverse_path(robot=robot, commands=args.commands)
    distance = calculate_distance(
        current_position=(robot.current_x, robot.current_y),
        start_position=(robot.start_x, robot.start_y))
    end = time.time() - start

    verbose_print('current direction - ', robot.direction)
    verbose_print('current position  - ', (robot.current_x, robot.current_y))
    verbose_print('distance to start - ', distance)
    verbose_print('time taken - ', end, 'seconds')

    print(distance)
