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
    M_str = "110BA66C C954BE96 3A7831D9 D9A3D1D3 9B8EC3"
    M = int(delete_space(M_str), 16)
    print('Plaintext M =', add_space(format(M, 'x')))
    Mx, My = ECC.data_embedding(M)
    print('Mx =', add_space(format(Mx, 'x')))
    print('My =', add_space(format(My, 'x')))
    Pm = point.Point(Mx, My)

    Pa_x = int(delete_space('02 7AB13D6D 69847A9C CE9A84E5 DB1BDDD8 7F11F38C'), 16)
    nk = int(delete_space('8E07EB42 65F1200D 0745BCB3 E47EDD2D 23FBF571'), 16)

    # G is the given point
    G = point.Point(ECC.Gx, ECC.Gy)
    Pk = G.scalar_mul(nk)
    # select even or odd
    selector = Pa_x // 0x10000000000000000000000000000000000000000    # Pa = 2 or 3
    Pa_x = Pa_x % 0x10000000000000000000000000000000000000000

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
    print('<EC-ElGamal encryption>')
    Pk = int(delete_space('02 7AF4ED0D 220D9482 424E72FE 5A375C6B FC2B0743'), 16)
    Pb = int(delete_space('03 015A7D66 7CDA436F 401E6156 9109D753 ECD1F0B1'), 16)
    na = int(delete_space('246FF426 810C46F5 04EE9F2F C69BFA35 B02BA373'), 16)
    selector_Pk = Pk // 0x10000000000000000000000000000000000000000  # Pa = 2 or 3
    selector_Pb = Pb // 0x10000000000000000000000000000000000000000  # Pa = 2 or 3
    Pk_x = Pk % 0x10000000000000000000000000000000000000000
    Pb_x = Pb % 0x10000000000000000000000000000000000000000

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

