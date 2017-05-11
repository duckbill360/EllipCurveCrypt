# 105064506 鄭柏偉
# Elliptic Curve Cryptography


# IMPORTS
import ECC


def delete_space(string):
    lst = string.split(' ')
    output = ''
    for i in lst:
        output += i
    return output


def add_space(string):
    string = string[::-1]
    string = ' '.join(string[i:i + 8] for i in range(0, len(string), 8))
    return string[::-1]


if __name__ == '__main__':
    M_str = "E1DB763C 99248E66 0A4801A9 A973A1A3 6B5E93"
    M = int(delete_space(M_str), 16)
    print('Plaintext M =', add_space(format(M, 'x')))
    Mx, My = ECC.data_embedding(M)
    print('Mx =', add_space(format(Mx, 'x')))
    print('My =', add_space(format(My, 'x')))
