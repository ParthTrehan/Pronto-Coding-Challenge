import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--commands', type=str, required=True)
    return parser

if __name__ == '__main__':
    args = get_parser().parse_args()
    print(args.commands)