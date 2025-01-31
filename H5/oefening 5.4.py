def main():
    welcome()
    input ("press enter to continue")
    step_1()
    input("press enter to continue")
    step_2()
    input("press enter to continue")
    step_3()

def welcome():
    print('Welcome')
    print('This program tells you how to disassemble an ACME laundry dryer.')
    print('There are 3 steps in the process.')

def step_1():
    print('Step 1:')
    print('Unplug the dryer and move it away from the wall.')

def step_2():
    print('Step 2:')
    print('Remove the six screws from the back of the dryer.')

def step_3():
    print('Step 3:')
    print('Remove the back panel.')

main()