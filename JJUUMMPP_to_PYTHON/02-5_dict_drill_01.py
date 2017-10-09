# NATO_PHONETIC_ALPHABET = """
# A   Alfa
# B	Bravo
# C	Charlie
# D	Delta
# E	Echo
# F	Foxtrot
# G	Golf
# H	Hotel
# I	India
# J	Juliett
# K	Kilo
# L	Lima
# M	Mike
# N	November
# O	Oscar
# P	Papa
# Q	Quebec
# R	Romeo
# S	Sierra
# T	Tango
# U	Uniform
# V	Victor
# W	Whiskey
# X	X-ray
# Y	Yankee
# Z	Zulu
# –	Dash
# """

NATO_PHONETIC_ALPHABET = """
A   10462
B	2036
C	502573
D	12693
E	249205
F	923466
G	2345
H	3254
I	124093350
J	19293533
K	530
L	2
M	9
N	923647
O	60943
P	192
Q	053
R	402534
S	7694
T	94032454
U	2363017
V	40035
W	0
X	69
Y	793
Z	6643223
-	97
"""

def get_code_from_NPA(str_code):
    dict_code = {}
    list_data = str_code.strip().split('\n')
    for n in range(len(list_data)):
        b = list_data[n].strip().split()
        dict_code[b[0]] = b[1]
    return dict_code

dict_data = get_code_from_NPA(NATO_PHONETIC_ALPHABET)

input_word = str(input("Your Message: "))

def get_input_word(input_word):
    encoded_input = " ".join(input_word).strip().split()
    print(str(encoded_input) + '\n')
    return encoded_input

def print_output(encoded_input):
    print("Encoded Message: ", end="")
    for n in range(len(encoded_input)):
        answer = dict_data[encoded_input[n].upper()] + '8'
        print(answer, end="")
    print("\n")
# print(dict_data[input_word.upper()])

encoded_input = get_input_word(input_word)
print_output(encoded_input)

# def input_phrase():
#     pass
#     return phrase
#
# def check_phrase(phrase):
#     return checked_phrase
#
# def get_NPA_encode(word):
#     pass
#     return NPA_encode_word
