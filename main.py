import os
import argparse

def conceal(blanket, message):
    pass

def reveal(blanket, key):
    pass

def main():
    description = 'Hide a message inside another'
    parser = argparse.ArgumentParser(description=description,
                                     epilog='arguments --conceal and --reveal are mutually exclusive')

    # Arguments for which task to perform
    task_group = parser.add_mutually_exclusive_group(required=True)
    task_group.add_argument('-c','--conceal', action='store', nargs=2, type=str,
                       help='Conceal message inside blanket message',
                       metavar=('Blanket', 'Text'))
    task_group.add_argument('-r','--reveal', action='store', nargs=2, type=str,
                       help='Reveal message hidden in blanket message',
                       metavar=('Blanket', 'Key'))

    # Arguments for how to output
    output_group = parser.add_mutually_exclusive_group(required=False)
    output_group.add_argument('-s','--stdout', action='store_const', dest='type', const='s',
                       help='Output prints to stdout',)
    output_group.add_argument('-t','--txt', action='store_const', dest='type', const='t',
                       help='Output saves result into file in same location as blanket',)
    parser.set_defaults(type='s')

    args = parser.parse_args()

    print(args)

if __name__ == '__main__':
    main()
