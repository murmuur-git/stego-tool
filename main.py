"""
CLI tool to hide one message in another message

author: murmuur
"""
from libs import *

def init():
    """
    Sets up the CLI
    """
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
                       help='Output saves result into file',)
    parser.set_defaults(type='s')

    global ARGS
    ARGS = parser.parse_args()

def conceal(blanket_path, message_path, mode='s'):
    """
    Conceals a message inside a blanket message. Concealing is done by finding a
    key string that when combined with blanket message converts the charachters
    into the message starting with the first one. No actual work is done to the
    blanket message, so finding the hidden message or key is impossible without
    one or the other.
    """

    # Open files
    blanket = get_contents(blanket_path)
    message = get_contents(message_path)

    if blanket == None: # Checks if blanket_path exists:
        print(f'[{bcolor.WARNING}!{bcolor.WARNING}] Error 101: {blanket_path} does not exist')
    elif message == None: # Checks if message_path exists
        print(f'[{bcolor.WARNING}!{bcolor.WARNING}] Error 101: {message_path} does not exist')

    # Returns key
    if mode == 's': # Print to console
        print(xor_loop(blanket, message, hex_mode='o'))
    elif mode == 't': # Save as txt file
        outfile_path = os.getcwd()+'/output.txt'
        with open(outfile_path, 'w') as file:
            file.write(xor_loop(blanket, message))

def reveal(blanket_path, key_path, mode='s'):
    """
    Reveals a message concealed using conceal()
    """
    # Open files
    blanket = get_contents(blanket_path)
    key = ast.literal_eval(get_contents(key_path))

    if blanket == None: # Checks if blanket_path exists:
        print(f'[{bcolor.WARNING}!{bcolor.WARNING}] Error 101: {blanket_path} does not exist')
    elif key == None: # Checks if key_path exists
        print(f'[{bcolor.WARNING}!{bcolor.WARNING}] Error 101: {key_path} does not exist')

    # Returns key
    if mode == 's': # Print to console
        print(xor_loop(blanket, key, hex_mode='i'))
    elif mode == 't': # Save as txt file
        outfile_path = os.getcwd()+'/output.txt'
        with open(outfile_path, 'w') as file:
            file.write(xor_loop(blanket, key))

def main():
    init()

    if ARGS.conceal != None:
        conceal(ARGS.conceal[0], ARGS.conceal[1], mode=ARGS.type)
    elif ARGS.reveal != None:
        reveal(ARGS.reveal[0], ARGS.reveal[1], mode=ARGS.type)

    #print(ARGS)

if __name__ == '__main__':
    main()
