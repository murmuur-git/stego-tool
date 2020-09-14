"""
Helper functions for main.py

author: murmuur
"""

def is_valid_file(path):
    pass

def get_contents(path):
    """
    Gets contents in file given a relative path to where command was run

    Note: confidently works on macos file system, others unknown
    """

    with open(path, 'r') as file:
        pass

def xor_loop(primary_message, secondary_message):
    """
    Function loops through two strings and xors charachters by index

    Note: primary_message must be longer than secondary_message
    """

    if len(primary_message) < len(secondary_message):
        return None

    final_message = ''
    for i, char in enumerate(secondary_message):
        final_message += (chr(ord(primary_message[i]) ^ ord(char)))
    return final_message
