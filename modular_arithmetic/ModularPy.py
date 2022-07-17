import sys


class ModularOps:
    """
    A class for doing operations in quotient ring Z_{N}

    This class implements various operations like addition, subtraction,
    multiplication, exponentiation, eic. on elemnts x and y belonging to the
    quotient ring Z/NZ. This ring is a field when N is prime.

    self.N: Positive integer.
    Modulus of the ring.
    """

    def __init__(self, N):
        """
        Initialise the modulus of the ring.

        If the parameter N is not positive the modulus is taken
        to be the maximum integer supported by the system.

        N: The modulus as provided by the user.
        """
        if N <= 0:
            N = sys.maxsize
        self.N = N

    def add(self, x, y):
        """
        Return the sum of two elements belonging to Z/NZ

        x: Positive integer belonging to the set {0,..., N-1}
        y: Positive integer belonging to the set {0,..., N-1}
        """
        if (x < 0 or x >= self.N) or (y < 0 or y >= self.N):
            raise ValueError("Parameters must belong the ring Z/{}Z\n.".format(N))
        s = x + y
        if s >= self.N:
            s = s - self.N
        return s

    def subtract(self, x, y):
        """
        Return the difference of two elements belonging to Z/NZ

        x: Positive integer belonging to the set {0,..., N-1}
        y: Positive integer belonging to the set {0,..., N-1}
        """
        if (x < 0 or x >= self.N) or (y < 0 or y >= self.N):
            raise ValueError("Parameters must belong the ring Z/{}Z\n.".format(N))
        if y > x:
            x = x + self.N
        return x - y
