import os

blanket_path = os.path.join(os.path.expanduser('~'),input('Which file would you like to use as the blanket: '))

with open(blanket_path, 'r+') as file:
    blanket = file.read()
