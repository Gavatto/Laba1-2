class Rectangle():
    def __init__(self, length=1.0, width=1.0):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, value):
        if not isinstance(value, float):
            raise Exception()
        if value < 0.0 or value > 20.0:
            raise Exception()
        self._length = value

    @width.setter
    def width(self, value):
        if not isinstance(value, float):
            raise Exception()
        if value < 0.0 or value > 20.0:
            raise Exception()
        self._width = value


    def rectangle_area(self):
        return self.length * self.width

    def perimeter_area(self):
        return 2 * (self.length + self.width)


