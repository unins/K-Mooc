"""-------------------------------- U*S*S*R 2 C*C*C*P 3 --- List(array)
"""

a = """
Kim ke'ai = 000231-3314159
Lee Hehe = 160702-4181818
Park Monte = 880418-3079423
"""

# a_masked = []
# for n in range(len(b)):
#     a_masked.append(b[n][:-6] + "*" * 6)

def get_masked_data(unmasked):
    a_masked_str = ""
    list_data = unmasked.strip().split('\n')
    for n in range(len(list_data)):
        a_masked_str = a_masked_str + (list_data[n][:-6] + "*" * 6) + "\n"
    return a_masked_str

def main():
    masked_data = get_masked_data(a)

    print(type(masked_data))
    print(masked_data)
get_masked_data(a)
main()

"""-------------------------------- U*S*S*R 2 C*C*C*P 3.1 --- List(array)
"""

# a = [1, 2, 3, 4, 5]
#
# a[0:2] = ['a', 'b']
#
# print(a) #['a', 'b', 3, 4, 5]
#
# del a[0:3]
#
# print(a) #[4, 5]
#
# a[0:1] = [ ]
#
# print(a) #[5]

"""-------------------------------- U*S*S*R 2 C*C*C*P 3.2 --- tupple & dictionary
"""

dic1 = {1:'alpha', 3:'Charlie', 4:'Delta', 5:'Echo', 6:'Foxtrot'}

print(dic1)
dic1[1] = 'Alpha'
print(dic1)
dic1[2] = 'Bravo'
print(dic1)

c = list(dic1.keys())
v = list(dic1.values())
c.sort()
v.sort()

print(c)
print(v)

for n in range(len(c)):
    print("key %s is value %s" %(c[n], v[n]))
