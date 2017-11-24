#! python
import os
import time
import datetime

import io
import sys
""" make stdout environment cp494 to utf-8 [WINDOWS-7]
  1.BEFORE: 안녕세계 = �ȳ缼��
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = cp949        ---> change to 'utf-8'

  2.AFTER: 안녕세계 = 안녕세계
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = 'utf-8'
 """
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

SEPARATOR = '\n' + '__'*30 + '\n\n'
NUM_ARR = [
    [
    '.ooooo.',
    'oo..oo.',
    'oo..oo.',
    'oo..oo.',
    'ooooo..',],
    [
    '..oo...',
    'oooo...',
    '..oo...',
    '..oo...',
    'oooooo.',],
    [
    '.ooooo.',
    'o...oo.',
    '..ooo..',
    'ooo....',
    'oooooo.',],
    [
    '.ooooo.',
    '....oo.',
    '.oooo..',
    '...ooo.',
    'ooooo..',],
    [
    '...oo..',
    '.oo.o..',
    'oo..o..',
    'oooooo.',
    '....o..',],
    [
    '.ooooo.',
    'oo.....',
    'oooooo.',
    '....oo.',
    'ooooo..',],
    [
    '.ooooo.',
    'oo.....',
    'oooooo.',
    'oo..oo.',
    '.oooo..',],
    [
    'oooooo.',
    'o...oo.',
    '...oo..',
    '..oo...',
    '.oo....',],
    [
    '.ooooo.',
    'oo..oo.',
    '.oooo..',
    'oo..oo.',
    '.oooo..',],
    [
    '.ooooo.',
    'oo...o.',
    'oooooo.',
    '....oo.',
    'ooooo..',],
    ]
SYMBOL_ARR = [
    [
    '...',
    '...',
    '...',
    '...',
    '...',],
    [
    'oo.',
    'oo.',
    '...',
    'oo.',
    'oo.',],
    ]
AMPM_ARR = [
    [
    'ooo....',
    'o..o...',
    'ooo....',
    'o....o.',
    'o....o.',],
    [
    '.oo....',
    'o..o...',
    'oooo...',
    'o..o.o.',
    'o..o.o.',],
    ]

def parksungha(arr_name, change_flag=1):
    for f in range(5):
        if change_flag == 1:
            print(arr_name[f].replace('.',' ').replace('o','@'))
        else:
            print(arr_name[f].replace('.',' '))
    print('\n')


def main(change_flag=1):
    for n in range(10):
        parksungha(n, change_flag)

def get_2_digit_arr_list(num_1, num_2):
    a = []
    for n in range(5):
        a.append(num_1[n] + num_2[n])
    return a

mixed_digit = get_2_digit_arr_list(NUM_ARR[5], NUM_ARR[7])

for d in range(5):
    print(mixed_digit[d])
print('\n')


_1_arr = get_2_digit_arr_list(AMPM_ARR[1], NUM_ARR[1])
_2_arr = get_2_digit_arr_list(_1_arr, NUM_ARR[2])
_3_arr = get_2_digit_arr_list(_2_arr, SYMBOL_ARR[1])
_4_arr = get_2_digit_arr_list(_3_arr, SYMBOL_ARR[0])
_5_arr = get_2_digit_arr_list(_4_arr, NUM_ARR[2])
_6_arr = get_2_digit_arr_list(_5_arr, NUM_ARR[2])
_7_arr = get_2_digit_arr_list(_6_arr, SYMBOL_ARR[1])
_8_arr = get_2_digit_arr_list(_7_arr, SYMBOL_ARR[0])
_9_arr = get_2_digit_arr_list(_8_arr, NUM_ARR[4])
_10_arr = get_2_digit_arr_list(_9_arr, NUM_ARR[7])


_a_arr = get_2_digit_arr_list(AMPM_ARR[1], NUM_ARR[1])
_b_arr = get_2_digit_arr_list(_a_arr, NUM_ARR[2])
_c_arr = get_2_digit_arr_list(_b_arr, SYMBOL_ARR[1])
_d_arr = get_2_digit_arr_list(_c_arr, NUM_ARR[2])
_e_arr = get_2_digit_arr_list(_d_arr, NUM_ARR[2])

_f_arr = get_2_digit_arr_list(SYMBOL_ARR[0], SYMBOL_ARR[0])
_g_arr = get_2_digit_arr_list(_f_arr, SYMBOL_ARR[0])
_h_arr = get_2_digit_arr_list(_g_arr, NUM_ARR[4])
_i_arr = get_2_digit_arr_list(_h_arr, NUM_ARR[7])

parksungha(_10_arr, 0)
print()

parksungha(_e_arr, 1)
print()
parksungha(_i_arr, 1)
