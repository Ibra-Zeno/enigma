import random
import string
print('project Crypto')  # Aim is to encrypt and decrypt messages

# Create keys string


def enigma():
    keys = 'abcdefghijklmnopqrstuvwxyz )(*&'
    # Autogenerate values string by setting original string
    values = keys[-1] + keys[-2] + keys[:-2]

    # Create two dictionaries
    dict_e = {key: value for key, value in zip(keys, values)}
    dict_d = {value: key for key, value in zip(keys, values)}
    print(dict_e)
    print(dict_d)

    # User inputs message and mode (encrypt or decrypt)
    msg = input('Enter a message to send securely: ').lower()
    mode = input('Press "e" to encrypt and anything else to decrypt: ').lower()

    # encode/decode
    if mode == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg]).capitalize()
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg]).capitalize()
    print(new_msg)

    # return result
    return new_msg

# clean up


enigma()
