import random
""" file doc-string : Pici-Fermi-Beagles game
 comp. gives clues, 10 times.... like below
 ------------
 (1) Pico : correct but wrong position
 (2) Fermi : correct and right position
 (3) Beagles : neither correct nor postion
 """


def get_rand_num_to(digit):
    _rand_arr = [n for n in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(_rand_arr)
    # print(_rand_arr)                    # [1, 8, 4, 5, 2, 6, 3, 0, 7, 9]

    _rand_num = ''
    for n in range(digit):
        _rand_num += str(_rand_arr.pop())
    return _rand_num

def get_input():        # OUT = 'str'
    # num_str = input('Input your 3 digit Number  : ')
    return input('Input your 3 digit Number  : ')

def show_num_attribute(num_str):
    if num_str.isnumeric():
        print('....number...')

    if num_str.isalpha():
        print('....alphabet...')

    if num_str.isalnum():
        print('....alpha-numeric...')

def is_number_valid(num_str, digit, show_flag=0):
    if show_flag == 1:
        show_num_attribute(num_str)

    if num_str.isnumeric():
        if len(num_str) == 3:
            return True
        else:
            return False
    else:
        return False


while True:
    _your_number = get_input()
    print(_your_number)

    print(is_number_valid(_your_number, 3, 1))

    _comp_num = get_rand_num_to(3)
    print(_comp_num, '\n\n')
