import random

_a = random.randint(0, 9)
print('\nrandint =', _a)

_a = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print('\nrand.choice =', _a)

_a_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('\nbefore...', _a_arr)

for n in range(10):
    random.shuffle(_a_arr)
    print('shuffle!...', _a_arr)
