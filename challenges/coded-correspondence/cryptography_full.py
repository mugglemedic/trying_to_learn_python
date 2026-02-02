# import string
# alphabet = list(string.ascii_lowercase)
# caesar_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
# deciphered = []
#
#
# def find_index(char):
#     if char in [' ', ',', '?', '!']:
#         return char
#     else:
#         index = alphabet.index(char) + 10
#     if index >= 26:
#         new_index = index-26
#         return new_index
#     else:
#         return index
#
#
# def cesar_cipher_decode(cipher):
#     answer = []
#
#     for letter in cipher:
#         if letter in [' ', ',', '?', '!']:
#             return letter
#         else:
#             # breakpoint()
#             decode = find_index(letter)
#             answer.append(alphabet[decode])
#     return answer
#
#
# print(cesar_cipher_decode(caesar_message))
#######################################################
##################### REDO ############################
#######################################################

# DECODE Caesar

import string

alphabet = list(string.ascii_lowercase)
caesar_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
new = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
new2 = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'


def find_index(char, offset):
    index = alphabet.index(char) + offset
    if index >= 26:
        index -= 26
    elif index < 0:
        index += 26
    return index


def caesar_cipher_decode(cipher, offset):
    answer = []
    for letter in cipher:
        if letter in alphabet:
            decode_index = find_index(letter, offset)
            answer.append(alphabet[decode_index])
        else:
            answer.append(letter)
    return "".join(answer)


# print(caesar_cipher_decode(caesar_message, 10))
# print(caesar_cipher_decode(new, 10))
# print(caesar_cipher_decode(new2, 14))

# ENCODE

coded = "hello, vishal. i think you may be in need of the touching of grass. live well and prosper."


def send_message(message, offset):
    cryptic = []
    for letter in message:
        if letter in alphabet:
            indexed = alphabet.index(letter) - offset
            if indexed >= 26:
                indexed -= 26
            elif indexed < 0:
                indexed += 26
            cryptic.append(alphabet[indexed])
        else:
            cryptic.append(letter)
    return "".join(cryptic)
# print(send_message(coded, -10))

# print(caesar_cipher_decode(new, 10))
# print(caesar_cipher_decode(new2, 14))


# BRUTE FORCE DECODE

level_caesar = 'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'
trying = list(range(26))
for num in trying:
    foo = 'comment this out and uncomment the print to get it working'
#    print(f'Attempt #{num}: {caesar_cipher_decode(level_caesar, num)}')


# Vigenère

# notes:
# import alphabet
# define var list = []
# define cipher string var ""
#
# def decode(message, key)
# define the var to be returned - list []
# find key index
# for loop, index each letter in string
#    if/then for non letters
# <0 += 26
# >26 -= 26
# figure out a way to loop the key back over and over
# orginal index shifts by negative index of key
#
# append chars
# else append non alphabet
# return "".join(decoded variable)
vig_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vishal_vig_key = 'friends'


def decode_vig(message, key):
    key_index = []
    answer = []
    iteration = 0

    for letter in key:
        key_index.append(alphabet.index(letter))

    for item in message:
        if item not in alphabet:
            answer.append(item)
        else:                   # put this into its own function, ugly.
            if iteration >= len(key):
                iteration = 0
            indexed = (alphabet.index(item) + key_index[iteration])
            if indexed >= 26:
                indexed -= 26
            elif indexed < 0:
                indexed += 26
            answer.append(alphabet[indexed])
            iteration += 1
    return "".join(answer)


# print(decode_vig(vig_message, vishal_vig_key))
# strike that, reverse it.

def encode_vig(message, key):
    key_index = []
    answer = []
    iteration = 0

    for letter in key:
        key_index.append(alphabet.index(letter))

    for item in message:
        if item not in alphabet:
            answer.append(item)
        else:                   # put this into its own function, ugly.
            if iteration >= len(key):
                iteration = 0
            indexed = (alphabet.index(item) - key_index[iteration])
            if indexed >= 26:
                indexed -= 26
            elif indexed < 0:
                indexed += 26
            answer.append(alphabet[indexed])
            iteration += 1
    return "".join(answer)


print(encode_vig('there were a lot of debugging steps and code cleaning i had to do for that decoder. This is way easier.', 'purple'))
