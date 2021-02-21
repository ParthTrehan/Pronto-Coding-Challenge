import argparse
import re
import time
import sys


class Robot:
    '''
    This is the main Robot class that covers all the robot related 
    variables, such as robot's current_position and direction, and 
    methods such as move and rotate. This class also includes the 
    function for calculating the distance of the robot from the 
    start point.
    '''

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

    def traverse(self, commands):
        '''
        This function is the head function for traversing the robot.
        This function takes string commands as input and traverses
        the robot.
        '''
        commands_arr = commands.split(',')
        for command in commands_arr:
            if command[0] in ['F', 'B']:
                self.move(command)
            else:
                self.rotate(command)

    def move(self, command):
        '''
        This functions moves th robot based on the single command 
        (for example F3 or B1). The moment of the robot is calculated 
        based on the current robot's direction.
        '''
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

    def rotate(self, command):
        '''
        This rotates the robot based on the single command (for
        example L3 or R1). The robot is rotated based on the current
        robot's direction.
        '''
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
        '''
        This function calculates the robot's distance form the starting
        point of the robot. This is implemented by calculating manhattan
        distance between the two points.
        '''
        return (abs(self.current_x-self.start_x)
                + abs(self.current_y-self.start_y))


def get_parser():
    prog = """robot.py"""

    description = """
                        DESCRIPTION:
    This is a simple program that takes a string of commands 
    as inputs in order to move a robot. These commands will 
    be  in the format <command><number> and the program can 
    take multiple commands for eg: "F1,R1,B2,L1,B3". The 
    program traverses the robot and returns the robot's 
    distance from its starting point. The robot can only 
    move in 4 directions (North, East, South, West). For 
    simplicity of the program, the robot can only move in 
    1-9 units in a single command. Please refer README.md
    for more information on available commands, arguments
    and design process.

    """
    commands_help = """
    a string of comma-separated commands eg: "F1,R1,B2,L1,B3"
    """
    parser = argparse.ArgumentParser(
        prog=prog,
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter,)
    parser.add_argument('--verbose', '-v',
                        action='store_true', default=False,
                        help='display more information about the robot traversal')
    parser.add_argument('--commands', '-c', type=str,
                        required=True, help=commands_help)
    return parser


def error(err):
    sys.stderr.write('error: ' + err)
    sys.exit(0)


def commands_validator(commands):
    '''
    This function validates the command line arguments. This functions
    constraints the user to use available arguments and units.
    '''
    if not(re.match(pattern="^([F|B|R|L][1-9])(,[F|B|R|L][1-9])*$",
                    string=commands)):
        error('Invalid input commands')


def main():
    '''
    This is the main function that is used to parse the command from the
    CLI arguments and traverse the robot.
    '''
    args = get_parser().parse_args()
    verbose_print = print if args.verbose else lambda *a, **k: None

    start = time.time()
    robot = Robot(current_position=(0, 0), direction='N')
    commands_validator(args.commands)
    robot.traverse(commands=args.commands)
    distance = robot.calculate_distance()
    end = time.time() - start

    verbose_print('\n##################### Verbose ######################')
    verbose_print('Current direction - ', robot.direction)
    verbose_print('Current position  - ', (robot.current_x, robot.current_y))
    verbose_print('Distance to start - ', distance)
    verbose_print('Time taken - ', end, 'seconds')
    verbose_print('#####################################################\n')

    sys.stdout.write(str(distance))
    sys.exit(1)

if __name__ == '__main__':
    main()
