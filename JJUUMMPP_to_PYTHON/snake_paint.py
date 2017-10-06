a = "012345"
b = ' ' * 4 + '.' + ' ' * 4
c = '.' * 50

def numbering(tabs):
    ruler = tabs+('  '+ b.join(a))+"\n"+tabs+('   '+'1234567890' * 5)
    return ruler

def middle_body(tabs):
    potato = ""
    for n in range(24):
        potato = potato + tabs + ("%2d %s %2d" %(n+1, c, n+1))+"\n"
    potato = potato + tabs + ("%2d %s %2d" %(25, c, 25))
    return potato

def main():
    for n in range(3):
        tabs = "\t" * n
        d = numbering(tabs)
        e = middle_body(tabs)
        print(d)
        print(e)
        print(d+"\n\n\n")

# print(tabs + d)
# print(tabs + e)
# print(tabs + d)

# main()

"""------------------------------------ U*S*S*R 2 -- C*C*C*P 4 ---
      TEXT ANIMATION
"""

# J = [
#         ['.....',
#         '.O...',
#         '.OOO.',
#         '.....',
#         '.....'],
#
#         ['.....',
#         '..OO.',
#         '..O..',
#         '..O..',
#         '.....'],
#
#         ['.....',
#         '.....',
#         '.OOO.',
#         '...O.',
#         '.....'],
#
#         ['.....',
#         '..O..',
#         '..O..',
#         '.OO..',
#         '.....'],
#         ]
J = [
        ['.....',
        '.OOO.',
        '..O..',
        '.OOO.',
        '.....'],[

        '.....',
        '..O..',
        '.OOO.',
        '..O..',
        '.....'],
        ]

import time

# print(type(J))
# print(len(J))
# print(J[0])
# print("\n\n\n")

def clear():
    print("\n\n"*100)

while True:
    for m in range(len(J)):
        clear()
        for n in range(len(J[m])):
            a = J[m][n].replace(".", "　").replace("O", "■")
            print(a)
        print('\n')
        time.sleep(1)
