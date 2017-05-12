import ECC


class Point:

    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # point inverse
    def inverse(self):
        self.y = ECC.p - self.y

    # point addition
    def add(self, input):
        output = Point(0, 0)
        lamb = (((input.y - self.y) % ECC.p) // ((input.x - self.x) % ECC.p)) % ECC.p
        output.x = (lamb ** 2 - self.x - input.x) % ECC.p
        output.y = (ECC.p - self.y + lamb * ((self.x - output.x) % ECC.p)) % ECC.p

        return output

    # point doubling
    def doubling(self):
        output = Point(0, 0)
        lamb = (((3 * (self.x ** 2) + ECC.a) % ECC.p) // ((2 * self.y) % ECC.p)) % ECC.p
        output.x = (lamb ** 2 - 2 * self.x) % ECC.p
        output.y = (ECC.p - self.y + lamb * ((self.x - output.x) % ECC.p)) % ECC.p

        return output

    def scalar_mul(self, b):
        output = Point(0, 0)
        D = Point(0, 0)
        str = bin(b)[2:]

        for i in str:
            D = D.doubling()
            if int(i) == 1:
                D = D.add(self)
        return D

    def show(self):
        print(format(self.x, 'x'))
        print(format(self.y, 'x'))
