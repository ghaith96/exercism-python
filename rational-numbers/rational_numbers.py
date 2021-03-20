from __future__ import division
from math import gcd


class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise Exception("denom can't be 0.")

        self.numer = numer if denom > 0 else -numer
        self.denom = abs(denom)

        self.reduce()

    def reduce(self):
        greatest_common_div = gcd(self.numer, self.denom)
        self.numer //= greatest_common_div
        self.denom //= greatest_common_div

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __add__(self, other):
        """
        The sum of two rational numbers r1 = a1/b1 and r2 = a2/b2 is r1 + r2 = a1/b1 + a2/b2 = (a1 * b2 + a2 * b1) / (b1 * b2).
        """

        return Rational(
            (self.numer * other.denom) + (other.numer * self.denom),
            self.denom * other.denom,
        )

    def __sub__(self, other):
        """
        The difference of two rational numbers r1 = a1/b1 and r2 = a2/b2 is r1 - r2 = a1/b1 - a2/b2 = (a1 * b2 - a2 * b1) / (b1 * b2).
        """

        return Rational(
            (self.numer * other.denom) - (other.numer * self.denom),
            self.denom * other.denom,
        )

    def __mul__(self, other):
        """
        The product (multiplication) of two rational numbers r1 = a1/b1 and r2 = a2/b2 is r1 * r2 = (a1 * a2) / (b1 * b2).
        """

        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        """
        Dividing a rational number r1 = a1/b1 by another r2 = a2/b2 is r1 / r2 = (a1 * b2) / (a2 * b1) if a2 * b1 is not zero.
        """

        return Rational(self.numer * other.denom, other.numer * self.denom)

    def __abs__(self):
        """
        The absolute value |r| of the rational number r = a/b is equal to |a|/|b|.
        """

        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        """
        Exponentiation of a rational number r = a/b to a non-negative integer power n is r^n = (a^n)/(b^n).

        Exponentiation of a rational number r = a/b to a negative integer power n is r^n = (b^m)/(a^m), where m = |n|.
        """

        abs_power = abs(power)
        new_numer = self.numer ** abs_power
        new_denom = self.denom ** abs_power
        return (
            Rational(new_numer, new_denom)
            if power > 0
            else Rational(new_denom, new_numer)
        )

    def __rpow__(self, base):
        """
        Exponentiation of a rational number r = a/b to a real (floating-point) number x is the quotient (a^x)/(b^x), which is a real number.

        Exponentiation of a real number x to a rational number r = a/b is x^(a/b) = root(x^a, b), where root(p, q) is the qth root of p.
        """

        return pow(base ** self.numer, 1 / self.denom)
