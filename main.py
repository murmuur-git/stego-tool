from libs import *

def conceal(blanket, message, mode):
    """
    Conceals a message inside a blanket message. Concealing is done by finding a
    key string that when combined with blanket message converts the charachters
    into the message starting with the first one. No actual work is done to the
    blanket message, so finding the hidden message or key is impossible without
    one or the other.
    """
    xor_loop(blanket, message)
    

def reveal(blanket, key):
    pass

def init():
    description = 'Hide a message inside another'
    parser = argparse.ArgumentParser(description=description,
                                     epilog='arguments --conceal and --reveal are mutually exclusive')

    # Arguments for which task to perform
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-c','--conceal', action='store', nargs=2, type=str,
                       help='Conceal message inside blanket message',
                       metavar=('Blanket', 'Text'))
    mode_group.add_argument('-r','--reveal', action='store', nargs=2, type=str,
                       help='Reveal message hidden in blanket message',
                       metavar=('Blanket', 'Key'))

    # Arguments for how to output
    output_group = parser.add_mutually_exclusive_group(required=False)
    output_group.add_argument('-s','--stdout', action='store_const', dest='type', const='s',
                       help='Output prints to stdout',)
    output_group.add_argument('-t','--txt', action='store_const', dest='type', const='t',
                       help='Output saves result into file in same location as blanket',)
    parser.set_defaults(type='s')

    global ARGS
    ARGS = parser.parse_args()

def main():
    init()

    blanket = 'Hello, World! How have you been?'
    message = 'Goodbye, World! D:'

    conceal(blanket, message, ARGS.type)

    print(ARGS)

if __name__ == '__main__':
    main()
