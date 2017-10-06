"""-------------------------------- U*S*S*R 2 C*C*C*P 1 --- List(array)
"""

a = """
Kim ke'ai = 000231-3314159
Lee Hehe = 160724-4181818
"""

b = a.strip().split('\n')

# print(b)
print(b[0][:-6] + '*' * 6)
print(b[1][:-6] + '*' * 6)

a_masked = """
%s
%s
""" %((b[0][:-6] + '*' * 6), (b[1][:-6] + '*' * 6))
print(a_masked)
