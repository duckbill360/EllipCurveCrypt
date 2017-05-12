# 105064506 鄭柏偉
# Elliptic Curve Cryptography


# IMPORTS
import ECC
import point


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
    print('<EC-ElGamal encryption>')
    M_str = "2923BE84 E16CD6AE 529049F1 F1BBE9EB B3A6DB"
    M = int(delete_space(M_str), 16)
    print('Plaintext M =', add_space(format(M, 'x')))
    Mx, My = ECC.data_embedding(M)
    print('Mx =', add_space(format(Mx, 'x')))
    print('My =', add_space(format(My, 'x')))
    P = point.Point(Mx, My)

    G = point.Point(ECC.Gx, ECC.Gy)
    A = point.Point(ECC.a, ECC.b)
    G = G.add(A)
    G.show()
