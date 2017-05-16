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
    M = int(delete_space(input('Plaintext M = ')), 16)
    Pa_x = int(delete_space(input('Pa = ')), 16)
    nk = int(delete_space(input('nk = ')), 16)
    Mx, My = ECC.data_embedding(M)
    print('Mx =', add_space(format(Mx, 'x')))
    print('My =', add_space(format(My, 'x')))
    Pm = point.Point(Mx, My)

    # G is the given point
    G = point.Point(ECC.Gx, ECC.Gy)
    Pk = G.scalar_mul(nk)
    # select even or odd
    mask = 0x10000000000000000000000000000000000000000
    selector = Pa_x // mask    # Pa = 2 or 3
    Pa_x = Pa_x % mask

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
    print('\n<EC-ElGamal encryption>')
    Pk = int(delete_space(input('Pk = ')), 16)
    Pb = int(delete_space(input('Pb = ')), 16)
    na = int(delete_space(input('na = ')), 16)
    selector_Pk = Pk // mask  # Pa = 2 or 3
    selector_Pb = Pb // mask  # Pa = 2 or 3
    Pk_x = Pk % mask
    Pb_x = Pb % mask

    # choose Pk_y
    value = (Pk_x ** 3 + ECC.a * Pk_x + ECC.b) % ECC.p
    r = ECC.sqrt_p_3_mod_4(value, ECC.p)
    Pk_y = 0
    if selector_Pk == 2 and r % 2 == 0:
        Pk_y = r
    elif selector_Pk == 2 and r % 2 == 1:
        Pk_y = ECC.p - r
    elif selector_Pk == 3 and r % 2 == 0:
        Pk_y = ECC.p - r
    elif selector_Pk == 3 and r % 2 == 1:
        Pk_y = r
    Pk = point.Point(Pk_x, Pk_y)

    # choose Pb_y
    value = (Pb_x ** 3 + ECC.a * Pb_x + ECC.b) % ECC.p
    r = ECC.sqrt_p_3_mod_4(value, ECC.p)
    Pb_y = 0
    if selector_Pb == 2 and r % 2 == 0:
        Pb_y = r
    elif selector_Pb == 2 and r % 2 == 1:
        Pb_y = ECC.p - r
    elif selector_Pb == 3 and r % 2 == 0:
        Pb_y = ECC.p - r
    elif selector_Pb == 3 and r % 2 == 1:
        Pb_y = r
    Pb = point.Point(Pb_x, Pb_y)

    Pk = Pk.scalar_mul(na)
    Pk.y = ECC.p - Pk.y

    Pm = Pb.add(Pk)
    print('Plaintext =', add_space(format(Pm.x, 'x'))[:-2])
