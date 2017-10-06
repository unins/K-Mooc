"""------------------------------------ C*C*C*P 1 --- NUMBERS
(1) INTEGER
(2) FLOAT
(3) Octa, Bin, Hexa
"""
def cccp1():
    a = 3.1415926535897932384626433832950288419716939937510582097494459
    b = 2
    c = a / b

    print(c)
    print(int(c))

    d = int(c)
    print(d)

    e = float(d)
    print(e)

    print(0b_1110)
# cccp1()

"""------------------------------------ C*C*C*P 2 --- OPERATORS
+ - * /
% ** //
"""

for n in range(7):
    print(7%(n+1))

for n in range(10000):
    print("16의 %2d제곱 =" %n, 16**n)

for n in range(10, 0, -1):
    print("10나누기%2d은(는)%2d입니다" %(n, 10//n))
