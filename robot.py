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
    parser.add_argument('-c', '--commands', type=str,
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
    commands_validator(args.commands)
    
    print(args.commands)
