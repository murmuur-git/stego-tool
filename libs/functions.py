"""
Helper functions for main.py

author: murmuur
"""
import os.path
from os import path

def get_contents(file_path):
    """
    Gets contents in file given a relative path to where command was run

    Note: confidently works on macos file system, others unknown
    """
    if path.exists(file_path) == False:
        return None

    with open(file_path, 'r') as file:
        return file.read()

def xor_loop(primary_message, secondary_message, hex_mode=None):
    """
    Function loops through two strings and xors charachters by index

    Notes:
        * primary_message must be longer than secondary_message
        * if hex_mode is i then takes secondary_message input as hex, if o then outputs list of hex
    """

    if len(primary_message) < len(secondary_message):
        return None


    if hex_mode == 'i':
        final_message = ''
        for i, char in enumerate(secondary_message):
            final_message += (chr(ord(primary_message[i]) ^ int(char, 16) ))
        return final_message
    elif hex_mode == 'o':
        final_hex = []
        for i, char in enumerate(secondary_message):
            final_hex.append(hex((ord(primary_message[i]) ^ ord(char) )))
        return final_hex
    else:
        final_message = ''
        for i, char in enumerate(secondary_message):
            final_message += (chr(ord(primary_message[i]) ^ ord(char)))
        return final_message
