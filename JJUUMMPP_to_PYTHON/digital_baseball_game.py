import random, os


def get_digit():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(digits)
    final_digit = ''
    for n in range(3):
        final_digit = final_digit + (str(digits[n-1]))
    return final_digit

def ask_number():
    ask = (input('input your number: '))
    return ask

def is_ask_str_check(ask_str, digit):
    if len(ask_str) == 3:
        if ask_str.isnumeric():
            return True
        else:
            print('\nERROR!')
            print('-+' * 40)
            print('input must be a number')
            return False
    else:
        print('\nERROR!')
        print('-+' * 40)
        print('number must be 3 digit')
        return False



answer = (get_digit())
print(answer)

while True:
    ask = ask_number()

    if is_ask_str_check(ask, 3):
        break
    else:
        pass


print(ask)
print(type(ask))



    #
    #
    #     if int(ask) < 10**(digit-1):
    #         return True
    #         print('\nERROR!')
    #         print('-+' * 40)
    #         print('number must be 3 digit')
    #         return False
    #     else:
    #         return True
    # else:
    #     print('\nERROR!')
    #     print('-+' * 40)
    #     print('input must be a number')
    #     return False
