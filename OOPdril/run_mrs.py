import mrs_code as mc
morse = mc.get_morse_dict()
sentence = "REQUEST ARTILLERY LINE 1 9 GRID LINE"
encode = "..-. .-"

def upper_case(sentence):
    sentence = sentence.upper()
    sentence = sentence.strip()
    return sentence

def make_morse(sentence):
    sentence = upper_case(sentence)
    decode = ""

    for n in range(len(sentence)):
        if sentence[n] == ' ':
            decode = decode + "   "
        else:
            decode = decode + morse[sentence[n]] + " "

    print("Sentence = ", sentence)
    print("Decode = ", decode)

def make_sentence(encode):
    decode = ""
    find_key = ''
    num_fk = 0

    arr_key = morse.keys()
    arr_value = morse.values()
    arr_encode= encode.split()

    for n in range(len(arr_encode)):
        find_key = arr_encode[n]
        for x in range(len(arr_value)):
            if find_key == list(arr_value)[x]:
                num_fk = x
                break
        decode = decode + list(arr_key)[num_fk]
    print(encode)
    print(decode)

def main():
    make_morse(sentence)
    print()
    make_sentence(encode)

if __name__ == '__main__':
    main()
