from libs.objects import *

def assert_equals(name, expected, actual):
    try:
        assert(expected == actual)
        print(f'    [{bcolors.OKGREEN}+{bcolors.ENDC}] Passed, {name} is {expected}')
    except:
        print(f'    [{bcolors.FAIL}!{bcolors.ENDC}] Failed, {name} is {actual}, expected {expected}')

def run_test(test_function):
    if callable(test_function):
        print(f'[{bcolors.OKBLUE}~{bcolors.ENDC}] Running {test_function.__name__}...')
        test_function()
    else:
        print(f'[{bcolors.WARNING}!{bcolors.ENDC}] Error: {test_function.__name__} failed to run, not function')
