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
    # ENCRYPTION
    print('<EC-ElGamal encryption>')
    M_str = "E1DB763C 99248E66 0A4801A9 A973A1A3 6B5E93"
    M = int(delete_space(M_str), 16)
    print('Plaintext M =', add_space(format(M, 'x')))
    Mx, My = ECC.data_embedding(M)
    print('Mx =', add_space(format(Mx, 'x')))
    print('My =', add_space(format(My, 'x')))
    Pm = point.Point(Mx, My)

    Pa = int(delete_space('03 7E3966DF 631F4871 3E61F0B7 0E1B5F77 C8A5B41B'), 16)
    nk = int(delete_space('5ED7BB12 35C1F0DD D7158C83 B44EADFD F3CBC541'), 16)

    # G is the given point
    G = point.Point(ECC.Gx, ECC.Gy)
    Pk = G.scalar_mul(nk)
    # select even or odd
    selector = Pa // 0x10000000000000000000000000000000000000000    # Pa = 2 or 3
    Pa_x = Pa % 0x10000000000000000000000000000000000000000

    # find the whole Pa
    value = (Pa_x ** 3 + ECC.a * Pa_x + ECC.b) % ECC.p
    r = ECC.sqrt_p_3_mod_4(value, ECC.p)
    Pa_y = 0
    if selector == 2 and r % 2 == 0:
        Pa_y = r
    elif selector == 2 and r % 2 == 1:
        Pa_y = ECC.p - r
    elif selector == 3 and r % 2 == 0:
        Pa_y = ECC.p - r
    elif selector == 3 and r % 2 == 1:
        Pa_y = r
    Pa = point.Point(Pa_x, Pa_y)

    Pb = Pm.add(Pa.scalar_mul(nk))
    print('Cm = {Pk, Pb} = {', add_space(format(Pk.x, 'x')), ',', add_space(format(Pb.x, 'x')), '}')

    # DECRYPTION

    # G = point.Point(ECC.Gx, ECC.Gy)
    # A = point.Point(ECC.a, ECC.b)
    # print(add_space(format(pow(ECC.a - ECC.Gx, ECC.p - 2, ECC.p), 'x')))