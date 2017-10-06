"""------------------------------------ U*S*S*R 2 -- C*C*C*P 1 ---
"""

def cccp1():
    a = """
            O
           /|V
            |
           /|
    """

    print(a)

    b = "\n        O\n       /|V\n        |\n       /|\n"

    print(b)

    c = "\"PlayerUnknown's BATTLEGROUND\" is Game made in Korea"
    d = "WARNING: CRITICAL DAMAGE in sys.dll\n"
    e = "ERROR: cannot find sint001.dll\n"

    f = (d + e) * 5
    print(c)
    print(f)
# cccp1()

"""------------------------------------ U*S*S*R 2 -- C*C*C*P 2 ---
"""
def cccp2():
    # a = "3.14159265358979323846264338327950288419716939937510582097494459"
    a = 789654312
    b = len(str(a))
    print(a)
    print("I know %s digits of Pi!" %(b-2))

    c = '   Wehrmacht and Commonwealth   '

    print(c.count('m'))
    print(c.find('w'))
    print('n'.join(c))
    print(c.split(' '))
    print(c, "numbers = %d" %len(c))
    print(c.strip(), "numbers = %d" %len(c.strip()))
cccp2()
