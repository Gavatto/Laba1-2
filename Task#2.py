from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=2):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise Exception()
        self._numerator = value

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise Exception()
        if value == 0:
            raise ValueError()
        self._denominator = value

    def __str__(self):
        common_denominator = gcd(self.numerator, self.denominator)
        self.numerator //= common_denominator
        self.denominator //= common_denominator
        return f"{self.numerator} / {self.denominator}"

    def float_value(self):
        return self.numerator / self.denominator