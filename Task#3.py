class Product:

    def __int__(self, price, size, description):
        self.price = price
        self.size = size
        self.description = description

    @property
    def price(self):
        return self._price

    @property
    def size(self):
        return self._size

    @property
    def description(self):
        return self._description

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError()
        if value < 0.0:
            raise ValueError()
        self._price = value

    @size.setter
    def dimensions(self, size):
        if not isinstance(size, float):
            raise Exception()
        self._size = tuple(size)

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise Exception()
        self._description = description

    def __str__(self):
        return f"{self.price}, {self.size}, {self.description}"

class Customer:

    def __init__(self,  surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def patronymic(self):
        return self._patronymic

    @property
    def phone_number(self):
        return self._mobile_phone

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception()
        self._name = name

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise Exception()
        self._surname = surname

    @patronymic.setter
    def name(self, patronymic):
        if not isinstance(patronymic, str):
            raise Exception()
        self._patronymic = patronymic

    @phone_number.setter
    def phone_number(self, mobile_phone):
        if not isinstance(mobile_phone, str):
            raise Exception()
        self._mobile_phone = mobile_phone

    def __str__(self):
        return f"{self.surname} {self.name}. {self.patronymic}. ({self.mobile_phone})"

