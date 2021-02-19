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

    def traverse_path(self, commands):
        commands_arr = commands.split(',')
        for command in commands_arr:
            if command[0] in ['F', 'B']:
                self.move_robot(command)
            else:
                self.rotate_robot(command)

    def move_robot(self, command):
        if command[0] == 'F':
            if self.direction == 'N':
                self.current_y += int(command[1])
            elif self.direction == 'E':
                self.current_x += int(command[1])
            elif self.direction == 'S':
                self.current_y -= int(command[1])
            else:
                self.current_x -= int(command[1])
        else:
            if self.direction == 'N':
                self.current_y -= int(command[1])
            elif self.direction == 'E':
                self.current_x -= int(command[1])
            elif self.direction == 'S':
                self.current_y += int(command[1])
            else:
                self.current_x += int(command[1])

    def rotate_robot(self, command):
        direction_arr = ['N', 'E', 'S', 'W']
        direction_units = int(command[1])
        if command[0] == 'L':
            direction_index = (direction_arr.index(
                self.direction) - direction_units) % 4
            self.direction = direction_arr[direction_index]
        else:
            direction_index = (direction_arr.index(
                self.direction) + direction_units) % 4
            self.direction = direction_arr[direction_index]

    def calculate_distance(self):
        return (abs(self.current_x-self.start_x) + abs(self.current_y-self.start_y))


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


if __name__ == '__main__':
    args = get_parser().parse_args()
    verbose_print = print if args.verbose else lambda *a, **k: None

    start = time.time()
    robot = Robot(current_position=(0, 0), direction='N')
    commands_validator(args.commands)
    robot.traverse_path(commands=args.commands)
    distance = robot.calculate_distance()
    end = time.time() - start

    verbose_print('Current direction - ', robot.direction)
    verbose_print('Current position  - ', (robot.current_x, robot.current_y))
    verbose_print('Distance to start - ', distance)
    verbose_print('Time taken - ', end, 'seconds')

    print(distance)
