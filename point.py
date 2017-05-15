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
        denominator = (input.x - self.x) % ECC.p
        numerator = (input.y - self.y) % ECC.p
        lamb = (pow(denominator, ECC.p - 2, ECC.p) * numerator) % ECC.p
        output.x = (lamb ** 2 - self.x - input.x) % ECC.p
        output.y = (ECC.p - self.y + lamb * ((self.x - output.x) % ECC.p)) % ECC.p

        return output

    # point doubling
    def doubling(self):
        output = Point(0, 0)
        denominator = (2 * self.y) % ECC.p
        numerator = (3 * (self.x ** 2) + ECC.a) % ECC.p
        lamb = (pow(denominator, ECC.p - 2, ECC.p) * numerator) % ECC.p
        output.x = (lamb ** 2 - 2 * self.x) % ECC.p
        output.y = (ECC.p - self.y + lamb * ((self.x - output.x) % ECC.p)) % ECC.p

        return output

    def scalar_mul(self, b):
        D = Point(-1, -1)
        string = bin(b)[2:]

        for i in string:
            if D.x != -1:
                D = D.doubling()
            else:
                D = Point(-1, -1)

            if int(i) == 1:
                if D.x == -1:
                    D = self
                else:
                    D = D.add(self)

        return D

    def show(self):
        print('x :', add_space(format(self.x, 'x')))
        print('y :', add_space(format(self.y, 'x')))


def add_space(string):
    string = string[::-1]
    string = ' '.join(string[i:i + 8] for i in range(0, len(string), 8))
    return string[::-1]