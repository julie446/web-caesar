def rotate_character(char, rot):
    if char.isalpha() != True:
        encrypted = char
    else:
        encrypted = ''
        rotated_index = alphabet_position(char) + rot
        alphabetL = 'abcdefghijklmnopqrstuvwxyz'
        alphabetU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if char in alphabetL:
            if rotated_index < 26:
                encrypted = alphabetL[rotated_index]
            elif rotated_index >= 26:
                encrypted = alphabetL[rotated_index % 26]
        elif char in alphabetU:
            if rotated_index < 26:
                encrypted = alphabetU[rotated_index]
            elif rotated_index >= 26:
                encrypted = alphabetU[rotated_index % 26]
    return encrypted

def alphabet_position(letter):
    alphabetL = 'abcdefghijklmnopqrstuvwxyz'
    alphabetU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in alphabetL:
        return alphabetL.index(letter)
    elif letter in alphabetU:
        return alphabetU.index(letter)

def encrypt(text, rot):
    encrypted = ''
    for char in text:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            encrypted = encrypted + rotate_character(char, rot)
    return encrypted

def user_input_is_valid(cl_args):
    if len(cl_args) > 1:
        return cl_args[1].isdigit()
    else:
        return False
