class Student:
    def __init__(self, name, age, phone, country):
        self.name = name
        self.age = age
        self.phone = phone
        self.country = country

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value
    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, value):
        self._country = value