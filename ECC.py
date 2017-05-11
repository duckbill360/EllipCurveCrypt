# Elliptic Curve Cryptography
# General elliptic curve group over a prime field GF(p) can be specified as E: y^2=x^3+ax+b with point G.
# The general elliptic curve group can be uniquely determined by the quintuple (p,a,b,G,n).
# In this assignment, we fix the following parameters.
# PARAMETERS
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF7FFFFFFF  # p % 4 == 3
a = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF7FFFFFFC
b = 0x1C97BEFC54BD7A8B65ACF89F81D4D4ADC565FA45
Gx = 0x4A96B5688EF573284664698968C38BB913CBFC82
Gy = 0x23A628553168947D59DCC912042351377AC5FB32
n = 0x0100000000000000000001F4C8F927AED3CA752257

import numbers


# Find SQROOT in Zp where p = 3 mod 4
def sqrt_p_3_mod_4(a, p):
    r = pow(a, (p + 1) // 4, p)
    return r


# Input: (m-8)-bit binary data M
# Output: Point (Mx,My) on the elliptic curve
def data_embedding(M):
    Mx = M << 8

    while not is_Mx_on_curve(Mx):
        Mx += 1

    value = (Mx ** 3 + a * Mx + b) % p
    My = sqrt_p_3_mod_4(value, p)

    return Mx, My


def is_Mx_on_curve(Mx):
    value = (Mx ** 3 + a * Mx + b) % p
    r = sqrt_p_3_mod_4(value, p)
    if pow(r, 2, p) == value:
        return True
    else:
        return False
