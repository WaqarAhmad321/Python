# getters are used to make a method the property of the object but values can't be set
# setters are used to set a value in getters
class MyClass:
    def __init__(self, _value):
        self._value = _value

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10


obj = MyClass(10)
obj.ten_value = 100
print(obj.ten_value)
