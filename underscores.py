class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 12
        self.__baz = 13


test1 = Test()
print(test1)
print(test1.foo)  # will print
print(test1._bar)  # will print
# print(test1.__baz)  # Will not print as will throw an error stating no attribute
print(dir(test1))
