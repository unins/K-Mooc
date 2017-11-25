import time, os
import datetime

NUM_ARR = [
    [
    ' __ ',
    '|  |',
    '|__|',],
    [
    '    ',
    '   |',
    '   |',],
    [
    ' __ ',
    ' __|',
    '|__ ',],
    [
    ' __ ',
    ' __|',
    ' __|',],
    [
    '    ',
    '|__|',
    '   |',],
    [
    ' __ ',
    '|__ ',
    ' __|',],
    [
    ' __ ',
    '|__ ',
    '|__|',],
    [
    ' __ ',
    '|  |',
    '   |',],
    [
    ' __ ',
    '|__|',
    '|__|',],
    [
    ' __ ',
    '|__|',
    ' __|',],
    ]
SYMBOL_ARR = [
    [
    '  ',
    '  ',
    '  ',],
    [
    '   ',
    ' . ',
    ' . ',],
    ]
AMPM_ARR = [
    [
    ' __  ',
    '|__| ',
    '|   .',],
    [
    ' __  ',
    '|__| ',
    '|  |.',],
    ]

CONTROL_DICT = {
    '0' : NUM_ARR[0],
    '1' : NUM_ARR[1],
    '2' : NUM_ARR[2],
    '3' : NUM_ARR[3],
    '4' : NUM_ARR[4],
    '5' : NUM_ARR[5],
    '6' : NUM_ARR[6],
    '7' : NUM_ARR[7],
    '8' : NUM_ARR[8],
    '9' : NUM_ARR[9],
    '_' : SYMBOL_ARR[0],
    ':' : SYMBOL_ARR[1],
    'a' : AMPM_ARR[1],
    'p' : AMPM_ARR[0],
    }

def parksungha(arr_name, change_flag=1):
    for f in range(5):
        if change_flag == 1:
            print(arr_name[f].replace('.',' ').replace('o','@'))
        else:
            print(arr_name[f])
    print('\n')

def get_multi_mixed_arr(*arr_names):
    multi_arr = ['', '', '', '', '']
    for name in arr_names:
        multi_arr[0] += name[0]
        multi_arr[1] += name[1]
        multi_arr[2] += name[2]
    return multi_arr

def main():
    a = datetime.datetime.now()

    ampm = a.strftime("%p")
    hour = a.strftime("%H")
    minute = a.strftime("%M")
    second = a.strftime("%S")
    hour12 = a.strftime("%I")

    weekday = a.strftime("%A")

    _combine = a.strftime('%p %I:%M:%S - %B %d, %A')

    os.system("cls")
    print(a, '\n')
    print("%2s:%2s:%2s %2s   %s\n" %(hour, minute, second, ampm.lower(), weekday))
    print(_combine)
    if ampm == "AM":
        ampmnow = 1
    elif ampm == "PM":
        ampmnow = 0
    for n in range(3):
        print("%s  %s%s%s%s%s%s%s%s"%(
        AMPM_ARR[int(ampmnow)][n],
        NUM_ARR[int(hour12[0])][n],
        NUM_ARR[int(hour12[1])][n],
        SYMBOL_ARR[1][n],
        NUM_ARR[int(minute[0])][n],
        NUM_ARR[int(minute[1])][n],
        SYMBOL_ARR[1][n],
        NUM_ARR[int(second[0])][n],
        NUM_ARR[int(second[1])][n]))
    time.sleep(1)

_a = get_multi_mixed_arr(
    CONTROL_DICT['a'],
    CONTROL_DICT['1'],
    CONTROL_DICT['0'],
    CONTROL_DICT[':'],
    CONTROL_DICT['1'],
    CONTROL_DICT['8'],
    CONTROL_DICT[':'],
    CONTROL_DICT['5'],
    CONTROL_DICT['2'],
)

parksungha(_a, 0)


# while True:
#     main()
